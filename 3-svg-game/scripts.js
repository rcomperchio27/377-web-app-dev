let grid = [0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0
];

let solution = [0, 0, 0, 6, 0, 0, 8, 0, 4, 
                6, 0, 0, 0, 0, 0, 2, 0, 0, 
                0, 7, 8, 4, 2, 5, 6, 0, 0, 
                3, 0, 0, 0, 7, 0, 0, 6, 0, 
                0, 0, 5, 0, 4, 0, 1, 0, 0, 
                0, 0, 0, 1, 5, 0, 0, 0, 0, 
                7, 0, 0, 0, 3, 0, 0, 0, 0, 
                0, 2, 0, 0, 0, 0, 9, 0, 0, 
                9, 4, 0, 5, 0, 2, 0, 1, 3
];

let blanklist = [];

function createPuzzle(currentRow) {
    for (number = 0; number < 9; number++) {
        let numpicked = true;
        while (numpicked) {
            let num = Math.ceil(Math.random(0, 1) * 9);
            checkRow = (num != grid[(currentRow * 9) - 9] && num != grid[(currentRow * 9) - (1)] && num != grid[(currentRow * 9) - (2)] && num != grid[(currentRow * 9) - (3)] && num != grid[(currentRow * 9) - (4)]
            && num != grid[(currentRow * 9) - (5)] && num != grid[(currentRow * 9) - (6)] && num != grid[(currentRow * 9) - (7)] && num != grid[(currentRow * 9) - (8)]);

            if (checkRow) {
                numpicked = false;
                grid[((currentRow - 1) * 9) + number] = num;
                
            }           
        }
        console.log(grid)
    }
    for (i = 0; i < $('#remove').val(); i++) {
        blanklist.push(Math.floor(Math.random(0, 1) * 81))
    }
    console.log(blanklist)
}

function loadPuzzle() {
    createPuzzle(1)
    let side = 64;
    let xpadding = 3;
    let ypadding = 3;
    let xtextIndent = 32;
    let ytextIndent = 40;

    for (row = 0; row < 9; row ++) {
        if (row % 3 == 0) {
            ypadding += 3;
        }
        xpadding = 3;
        for (column = 0; column < 9; column++) {
            let square = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
            let text = document.createElementNS('http://www.w3.org/2000/svg', 'text');
            if (column % 3 == 0 ) {
                xpadding += 3;
            } 
            text.setAttribute('y', (row * side) + ((3 * row) + ypadding + ytextIndent));
            text.setAttribute('x', (column * side) + ((3 * column) + xpadding + xtextIndent));
            text.setAttribute('id', ('text' + (parseInt(row * 9) + parseInt(column))));

            square.setAttribute('y', (row * side) + ((3 * row) + ypadding));
            square.setAttribute('x', (column * side) + ((3 * column) + xpadding));
            square.setAttribute('width', side);
            square.setAttribute('height', side);
            square.setAttribute('class', 'tile');
            square.setAttribute('id',('tile' + (parseInt(row * 9) + parseInt(column))));
            square.setAttribute('onclick', 'tileclicked(id)')

            svg.appendChild(square);
            svg.appendChild(text);

            blank = false
            for (i = 0; i < blanklist.length; i++) {
                if ((parseInt(row * 9) + parseInt(column)) == blanklist[i]) {
                    blank = true;
                }
            }

            if (blank == false) {
                text.innerHTML = String(solution[(parseInt(row * 9) + parseInt(column))]);
            }

            if ($('#text' + (parseInt(row * 9) + parseInt(column))).html() == '0') {
                $('#text' + (parseInt(row * 9) + parseInt(column))).html('')
                text.setAttribute('class', 'text');
            } else  {
                text.setAttribute('class', 'given');
            }
        }
    }
}

function tileclicked(tileid) {
    textid = 'text' + tileid.substring(4);
    console.log($('#' + textid).className)
    // if ($('#' + textid).getAttribute('class') != 'given') {
    //     if ($('#' + textid).html() == '') {
    //             $('#' + textid).html(0)
    //     }
    //     $('#' + textid).html((parseInt($('#' + textid).html()) + 1) % 10);
    //     if ($('#' + textid).html() == 0) {
    //         $('#' + textid).html('')
    //     }
    // }
    
}