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

    min = input[0];

    for (i = 0; i < input.length; i++) {
        sigfig = input[i].length;

        if (input[i].indexOf('.') != -1) {
            sigfig = input[i].length - 1;
        }
        if (sigfig < min) {
            min = sigfig;
        }
    }

    sigfig = parseFloat(min);
    console.log(sigfig);

    // decimals = 

    for (i = 0; i < input.length; i++) {
        measurments[i] = parseFloat(input[i]);
    }

    let measurmentssum = 0; 
    for (i = 0; i < measurments.length; i++) {
        measurmentssum += measurments[i];
    }

    barmeasurments = measurmentssum / (measurments.length);

    let xiBarxSq = 0;

    for (i = 0; i < measurments.length; i++) {
        xiBarx = Math.abs(measurments[i] - barmeasurments);
        xiBarx = Math.pow(xiBarx, 2);
        xiBarxSq += xiBarx;
    }
    
    
    
    let error = Math.sqrt(xiBarxSq / (measurments.length * (measurments.length - 1)));
    error = Math.round((error + Number.EPSILON) * sigfig) / sigfig
    console.log(error);
    console.log(measurments);
    console.log(barmeasurments);

    $('#RmsResult').html(barmeasurments + '&plusmn;' + error);
}

// testdata 54.84, 53.92, 54.46, 54.55, 54.30