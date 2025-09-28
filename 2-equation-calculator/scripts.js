function calculateDensity() {
    let mass = $('#densityMass').val();
    let length = $('#densityLength').val();
    let volume = (length * length * length);
    let density = (mass / volume);
    $('#densityResult').html(" The cube's density is: " + density + 'kg/m&sup3;');
}

function calculateVelocity() {
    let time = $('#velocityTime').val();
    let length = $('#velocityLength').val();
    let velocity = (length / time);
    $('#velocityResult').html(' The speed is: ' + velocity + 'm/s');
}

function calculateAcceleration() {
    let time = $('#accelerationTime').val();
    let length = $('#accelerationLength').val();
    let acceleration = (length / (time * time));
    $('#accelerationResult').html(' The acceleration is: ' + acceleration + 'm/s&sup2;');
}

function calculateRmsError() {
    let input = $('#rmsErrorMeasurements').val().split(/\s*,\s*/);
    let measurments = [];

    // sigfigmin = input[0];
    // decimin = 101 // only works up to 100 decimals

    // for (i = 0; i < input.length; i++) {
    //     sigfig = input[i].length;

    //     if (input[i].indexOf('.') != -1) {
    //         sigfig = input[i].length - 1;
    //         let num = input[i].split('.');
    //         console.log(num);

    //         if (parseInt(num[0]) > 0) {
    //             if (num[1].length < decimin) {
    //                 decimin = num[1].length;
    //             }
    //         }
            

    //     } else {
    //         decimin = 0;
    //     }
    //     if (sigfig < sigfigmin) {
    //         sigfigmin = sigfig;
    //     }
    // }

    // sigfig = parseFloat(sigfigmin);
    // console.log('sigfig:' + sigfig);
    // console.log(decimin);

    // defines sigfig and decimal values
    let sigfig = parseFloat($('#sigfig').val()) + 1;
    let decimal = 1 * (parseFloat($('#decimal').val()) + 1); 

    // changes from string to float
    for (i = 0; i < input.length; i++) {
        measurments[i] = parseFloat(input[i]);
    }

    // sum of all the measurements
    let measurmentssum = 0; 
    for (i = 0; i < measurments.length; i++) {
        measurmentssum += measurments[i];
    }
    let barmeasurments = Math.round((measurmentssum / (measurments.length)) * (10 ** sigfig), sigfig) / (10 ** sigfig);

    // sum of (x - xbar)squared
    let xiBarxSq = 0;
    for (i = 0; i < measurments.length; i++) {
        xiBarx = Math.abs(measurments[i] - barmeasurments);
        xiBarx = Math.pow(xiBarx, 2);
        xiBarxSq += xiBarx;
    }
    
    // final operations and rounding
    let error = Math.sqrt(xiBarxSq / (measurments.length * (measurments.length - 1)));
    error = Math.round((error * (10 ** decimal)), decimal) / (10 ** decimal);

    $('#RmsResult').html(' Your result is: ' + barmeasurments + '&plusmn;' + error);
}

// testdata 54.84, 53.92, 54.46, 54.55, 54.30