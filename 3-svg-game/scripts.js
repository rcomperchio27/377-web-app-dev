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

function createPuzzle() {
    let numpicked = true;
    grid[0] = Math.ceil(Math.random(0, 1) * 9);
    currentnum = grid[0]
    while (numpicked) {
        let num = Math.ceil(Math.random(0, 1) * 9);
        for (i = 1; i < 9; i++) {
            if (num != currentnum) {
                numpicked = false;
                grid[1] = num;
            }
        }
    }
    console.log(grid);
}

function loadPuzzle() {
    let side = 64;
    let xpadding = 3;
    let ypadding = 3;
    let border = 5;

    for (y = 0; y < 9; y ++) {
        xpadding = 3
        for (x = 0; x < 9; x++) {
            let square = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
            let text = document.createElementNS('http://www.w3.org/2000/svg', 'text');
            if (x % 3 == 0 ) {
                xpadding += 3
            } 
            if (y % 3 == 0) {
                ypadding -= 3

            }
            square.setAttribute('y', (y * side) + ((3 * y) + border + ypadding));
            square.setAttribute('x', (x * side) + ((3 * x) + border + xpadding));
            square.setAttribute('width', side);
            square.setAttribute('height', side);
            square.setAttribute('class', 'tile');
            square.setAttribute('id', (y * 9) + (x));
            svg.appendChild(square);
        }
    }

    $('#line').remove().appendTo('svg');

}