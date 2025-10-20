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
            text.setAttribute('class', 'text');
            text.setAttribute('id', ('text' + (row * 9) + (column)));

            square.setAttribute('y', (row * side) + ((3 * row) + ypadding));
            square.setAttribute('x', (column * side) + ((3 * column) + xpadding));
            square.setAttribute('width', side);
            square.setAttribute('height', side);
            square.setAttribute('class', 'tile');
            square.setAttribute('id',('tile' + (row * 9) + (column)));
            svg.appendChild(square);
            svg.appendChild(text);
            text.innerHTML = String(grid[(row * 9) + (column)]);
        }
    }

    $('#line').remove().appendTo('svg');

}