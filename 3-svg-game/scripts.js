// let solution = [0, 0, 0, 0, 0, 0, 0, 0, 0, 
//             0, 0, 0, 0, 0, 0, 0, 0, 0, 
//             0, 0, 0, 0, 0, 0, 0, 0, 0, 
//             0, 0, 0, 0, 0, 0, 0, 0, 0, 
//             0, 0, 0, 0, 0, 0, 0, 0, 0, 
//             0, 0, 0, 0, 0, 0, 0, 0, 0, 
//             0, 0, 0, 0, 0, 0, 0, 0, 0, 
//             0, 0, 0, 0, 0, 0, 0, 0, 0, 
//             0, 0, 0, 0, 0, 0, 0, 0, 0
// ];


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

let grid = [0, 0, 0, 6, 0, 0, 8, 0, 4, 
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

$(document).ready(function() {
    loadPuzzle();
});

function firstBox() {
    let firstbox = []
    for (number = 0; number < 9; number++) {
        let numpicked = true;
        while (numpicked) {
            let num = Math.ceil(Math.random(0, 1) * 9);
            checkBox = (num != solution[0] && num != solution[1] && num != solution[2] && num != solution[9] && num != solution[10]
            && num != solution[11] && num != solution[18] && num != solution[19] && num != solution[20]);

            if (checkBox) {
                numpicked = false;
                firstbox.push(num)
            }           
        }
    }
    for (i = 0; i < 3; i++) {
        solution[i] = firstbox[i]
        solution[i + 9] = firstbox[i + 3]
        solution[i + 18] = firstbox[i + 6]
    }
    console.log(solution)
}

function secondBox() {
    let secondbox = []
    for (number = 0; number < 9; number++) {
        let numpicked = true;
        while (numpicked) {
            let num = Math.ceil(Math.random(0, 1) * 9);
            let checkBox = (num != solution[0] && num != solution[1] && num != solution[2] && num != solution[9] && num != solution[10]
            && num != solution[11] && num != solution[18] && num != solution[19] && num != solution[20]);
            let checkleft = (solution[secondbox.length] != num)
            console.log(solution[secondbox.length])
            if (checkBox && checkleft) {
                numpicked = false;
                secondbox.push(num)
            }           
        }
    }
    for (i = 0; i < 3; i++) {
        solution[i] = secondbox[i]
        solution[i + 9] = secondbox[i + 3]
        solution[i + 18] = secondbox[i + 6]
    }
    console.log(solution)
}

function createPuzzle(currentRow) {
    firstBox()
    secondBox()
    // for (number = 0; number < 9; number++) {
    //     let numpicked = true;
    //     while (numpicked) {
    //         let num = Math.ceil(Math.random(0, 1) * 9);
    //         checkRow = (num != solution[(currentRow * 9) - 9] && num != solution[(currentRow * 9) - (1)] && num != solution[(currentRow * 9) - (2)] && num != solution[(currentRow * 9) - (3)] && num != solution[(currentRow * 9) - (4)]
    //         && num != solution[(currentRow * 9) - (5)] && num != solution[(currentRow * 9) - (6)] && num != solution[(currentRow * 9) - (7)] && num != solution[(currentRow * 9) - (8)]);

    //         if (checkRow) {
    //             numpicked = false;
    //             solution[((currentRow - 1) * 9) + number] = num;
                
    //         }           
    //     }
    //     console.log(solution)
    // }
    // for (i = 0; i < $('#remove').val(); i++) {
    //     blanklist.push(Math.floor(Math.random(0, 1) * 81))
    // }
    // console.log(blanklist)
}

function loadPuzzle() {
    createPuzzle()
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
                text.innerHTML = String(grid[(parseInt(row * 9) + parseInt(column))]);
            }

            if ($('#text' + (parseInt(row * 9) + parseInt(column))).html() == '0') {
                $('#text' + (parseInt(row * 9) + parseInt(column))).html('')
                square.setAttribute('class', 'tile');
                square.addEventListener('mouseover', function() {
                this.style.cursor = 'pointer';
                });
            } else  {   
                square.setAttribute('class', 'given');
            }
        }
    }
}

function tileclicked(tileid) {
    textid = 'text' + tileid.substring(4);
    if ($('#' + tileid).attr('class') == 'given') {
        return
    }
    if ($('#' + textid).html() == '') {
            $('#' + textid).html(0)
    }
    $('#' + textid).html((parseInt($('#' + textid).html()) + 1) % 10);
    if ($('#' + textid).html() == 0) {
        $('#' + textid).html('')
    }
    grid[tileid.substring(4)] = $('#' + textid).html()
    
}

function checkPuzzle() {
    for (i = 0; i < 81; i++) {
        if (grid[i] == solution[i] && $('#tile' + i).attr('class') != "given") {
            $('#tile' + i).css('fill', 'lightgreen');
        } else if ($('#tile' + i).attr('class') != "given") {
            $('#tile' + i).css('fill', 'lightcoral');
        }
        $('#tile' + i).attr("onclick", '')
    }
}
