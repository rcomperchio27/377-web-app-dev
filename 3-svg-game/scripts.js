function loadpuzzle() {
    let side = 64;
    let padding = 3;
    let border = 5

    for (y = 0; y < 9 * side; y += side) {
        for (x = 0; x < 9 * side; x += side) {
            let square = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
            if (y % 3 == 0) {
                square.setAttribute('y', y + ((padding) * (y / 50) + border));
            } else {
                square.setAttribute('y', y + (padding * (y / 50) + border));             
            }
            if (y % 3 == 0) {
                square.setAttribute('x', x + ((padding) * (x / 50) + border));
            } else {
                square.setAttribute('x', x + (padding * (x / 50) + border));             
            }            
            square.setAttribute('width', side);
            square.setAttribute('height', side);
            square.setAttribute('class', 'tile');
            square.setAttribute('fill', 'white');

            svg.appendChild(square);
        }
    }

    $('#line').remove().appendTo('svg');

}