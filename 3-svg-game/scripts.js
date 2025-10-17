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
    let padding = 3;
    let border = 5;

    for (y = 0; y < 9 * side; y += side) {
        for (x = 0; x < 9 * side; x += side) {
            let square = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
            let text = document.createElementNS('http://www.w3.org/2000/svg', 'text');
            square.setAttribute('y', y + ((padding) * (y / 50) + border));
            square.setAttribute('x', x + ((padding) * (x / 50) + border));
            square.setAttribute('width', side);
            square.setAttribute('height', side);
            square.setAttribute('class', 'tile');
            square.setAttribute('id', ((y / side) * 9) + (x / side));
            svg.appendChild(square);
        }
    }

    $('#line').remove().appendTo('svg');

}