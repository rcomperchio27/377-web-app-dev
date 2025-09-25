function calculateDensity() {
    let mass = $('#densityMass').val();
    let length = $('#densityLength').val();
    let volume = (length * length * length);
    let density = (mass / volume);
    $('#densityResult').html(density + 'kg/m&sup3;');
}

function calculateVelocity() {
    let time = $('#velocityTime').val();
    let length = $('#velocityLength').val();
    let velocity = (length / time);
    $('#velocityResult').html(velocity + 'm/s');
}

function calculateAcceleration() {
    let time = $('#accelerationTime').val();
    let length = $('#accelerationLength').val();
    let acceleration = (length / (time * time));
    $('#accelerationResult').html(acceleration + 'm/s&sup2;');
}

function calculateRmsError() {
    let input = $('#rmsErrorMeasurements').val().split(/\s*,\s*/);
    let measurments = [];

    for (i = 0; i < input.length; i++) {
        measurments[i] = parseFloat(input[i]);
    }
    let measurmentssum = 0; 
    for (i = 0; i < measurments.length; i++) {
        measurmentssum += measurments[i];
    }

    barmeasurments = measurmentssum / (measurments.length);

    

    console.log(measurments);
    console.log(barmeasurments);

}