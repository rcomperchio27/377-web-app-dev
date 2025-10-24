let currentPuzzle = 0;

let solutions = [[2, 3, 9, 6, 1, 7, 8, 5, 4, 
                6, 5, 4, 3, 9, 8, 2, 7, 1, 
                1, 7, 8, 4, 2, 5, 6, 3, 9, 
                3, 1, 2, 8, 7, 9, 4, 6, 5, 
                8, 6, 5, 2, 4, 3, 1, 9, 7, 
                4, 9, 7, 1, 5, 6, 3, 8, 2, 
                7, 8, 1, 9, 3, 4, 5, 2, 6, 
                5, 2, 3, 7, 6, 1, 9, 4, 8, 
                9, 4, 6, 5, 8, 2, 7, 1, 3], 
               [2, 9, 6, 5, 3, 8, 4, 1, 7, 
                8, 3, 7, 9, 4, 1, 6, 2, 5, 
                5, 1, 4, 6, 7, 2, 8, 3, 9, 
                3, 5, 1, 4, 8, 9, 2, 7, 6, 
                7, 4, 2, 1, 6, 3, 5, 9, 8, 
                6, 8, 9, 2, 5, 7, 3, 4, 1, 
                4, 2, 5, 7, 9, 6, 1, 8, 3, 
                1, 7, 8, 3, 2, 5, 9, 6, 4, 
                9, 6, 3, 8, 1, 4, 7, 5, 2],
               [9, 6, 8, 7, 3, 5, 1, 4, 2, 
                4, 5, 1, 9, 8, 2, 7, 3, 6, 
                3, 2, 7, 1, 6, 4, 8, 5, 9, 
                2, 3, 9, 6, 7, 1, 5, 8, 4, 
                1, 8, 4, 2, 5, 9, 6, 7, 3, 
                5, 7, 6, 8, 4, 3, 2, 9, 1, 
                6, 4, 2, 5, 9, 7, 3, 1, 8, 
                7, 1, 3, 4, 2, 8, 9, 6, 5, 
                8, 9, 5, 3, 1, 6, 4, 2, 7],
               [5, 4, 9, 2, 8, 6, 7, 1, 3, 
                2, 1, 7, 4, 3, 9, 8, 6, 5, 
                3, 8, 6, 7, 5, 1, 4, 9, 2, 
                1, 9, 3, 5, 7, 2, 6, 4, 8, 
                4, 7, 8, 9, 6, 3, 2, 5, 1, 
                6, 2, 5, 8, 1, 4, 3, 7, 9, 
                8, 5, 4, 3, 9, 7, 1, 2, 6, 
                7, 3, 1, 6, 2, 5, 9, 8, 4, 
                9, 6, 2, 1, 4, 8, 5, 3, 7],
               [9, 1, 5, 8, 6, 4, 7, 3, 2, 
                7, 6, 8, 2, 5, 3, 9, 4, 1, 
                3, 2, 4, 1, 7, 9, 5, 6, 8, 
                4, 9, 7, 6, 1, 2, 3, 8, 5, 
                1, 8, 2, 5, 3, 7, 6, 9, 4, 
                6, 5, 3, 9, 4, 8, 2, 1, 7, 
                8, 7, 6, 3, 2, 1, 4, 5, 9, 
                5, 4, 9, 7, 8, 6, 1, 2, 3, 
                2, 3, 1, 4, 9, 5, 8, 7, 6]]

let solution = solutions[0]

let grids = [['', '', '', 6, '', '', 8, '', 4, 
            6, '', '', '', '', '', 2, '', '', 
            '', 7, 8, 4, 2, 5, 6, '', '', 
            3, '', '', '', 7, '', '', 6, '', 
            '', '', 5, '', 4, '', 1, '', '', 
            '', '', '', 1, 5, '', '', '', '', 
            7, '', '', '', 3, '', '', '', '', 
            '', 2, '', '', '', '', 9, '', '', 
            9, 4, '', 5, '', 2, '', 1, 3], 
           ['', 9, '', '', '', '', 4, '', '', 
            '', '', '', '', '', '', 6, 2, '', 
            5, 1, '', 6, 7, '', '', 3, '', 
            '', 5, '', '', '', 9, '', 7, '', 
            '', '', 2, 1, 6, '', 5, 9, 8, 
            '', '', '', 2, '', '', '', '', '', 
            4, '', 5, '', 9, 6, '', '', 3, 
            '', '', 8, '', '', '', '', '', '', 
            9, 6, '', '', '', 4, 7, 5, ''],
           [9, '', '', '', 3, '', '', '', '', 
            4, '', '', '', 8, 2, '', '', '', 
            3, '', 7, '', '', 4, 8, 5, '', 
            '', 3, '', '', '', 1, '', '', 4, 
            '', '', 4, 2, 5, '', '', '', 3, 
            '', 7, '', 8, '', '', 2, '', 1, 
            6, '', '', 5, '', '', '', 1, '', 
            7, 1, 3, '', '', '', 9, '', '', 
            '', 9, 5, '', '', '', 4, '', ''], 
           [5, '', 9, 2, '', '', 7, 1, '', 
            '', '', '', 4, '', 9, 8, '', 5, 
            '', '', '', '', '', '', '', 9, 2, 
            '', '', '', '', 7, 2, 6, '', '', 
            '', 7, 8, '', 6, '', 2, '', '', 
            6, 2, '', '', 1, 4, '', '', 9, 
            8, 5, '', '', 9, '', '', '', '', 
            '', '', 1, 6, '', '', '', '', 4, 
            '', '', 2, '', '', '', 5, '', ''], 
           ['', 1, '', 8, 6, '', '', 3, '', 
            7, '', '', '', 5, '', '', '', '', 
            '', '', '', '', '', '', 5, 6, 8, 
            4, '', '', 6, 1, '', '', '', '', 
            1, '', '', '', 3, 7, '', 9, '', 
            '', '', '', 9, 4, '', 2, 1, 7, 
            8, '', '', '', '', '', 4, '', 9, 
            5, 4, '', 7, '', '', '', 2, 3, 
            2, '', '', '', 9, '', '', '', 6]]

let grid = grids[0];



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
}

function lastPuzzle() {
    if (currentPuzzle == 0) {
        currentPuzzle = 4
    } else {
        currentPuzzle -= 1
    }
    $('#currentPuzzle').html('Puzzle ' + String(currentPuzzle + 1))
    solution = solutions[currentPuzzle];
    grid = grids[currentPuzzle];
    loadPuzzle()
}

function nextPuzzle() {
    if (currentPuzzle == 4) {
        currentPuzzle = 0
    } else {
        currentPuzzle += 1
    }
    $('#currentPuzzle').html('Puzzle ' + String(currentPuzzle + 1))
    solution = solutions[currentPuzzle];
    grid = grids[currentPuzzle];
    loadPuzzle()
}

function loadPuzzle() {
    const svg = document.querySelector('svg');
    svg.innerHTML = '';
  
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

            text.innerHTML = String(grid[(parseInt(row * 9) + parseInt(column))]);

            if ($('#text' + (parseInt(row * 9) + parseInt(column))).html() == '0' || $('#text' + (parseInt(row * 9) + parseInt(column))).html() == '') {
                $('#text' + (parseInt(row * 9) + parseInt(column))).html('')
                square.removeAttribute('class')
                square.setAttribute('class', 'tile');
                square.addEventListener('mouseover', function() {
                this.style.cursor = 'pointer';
                });
            } else {   
                square.removeAttribute('class')
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
