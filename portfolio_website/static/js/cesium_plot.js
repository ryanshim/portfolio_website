// Collection of js functions to draw satellite positions in a Cesium world
function main_driver(tle) {
    $(document).ready(function() {
        tle = tle.replace(/&#34;/g, '"');   // replace ascii code &#34 to '"'
        tle = JSON.parse(tle);              // Parse string to json object

        let viewer = create_skybox();       // draw the cesium environment
        var points = viewer.scene.primitives.add(new Cesium.PointPrimitiveCollection());
        
        lla = get_positions(tle);
        plot_positions(lla, points);

        window.setInterval(function() {
            lla = get_positions(tle);
            plot_positions(lla, points);
        }, 2000);
    });
 }

// Create the skybox
function create_skybox() {
    // create new cesium globe
    var viewer = new Cesium.Viewer('cesiumContainer', {
        animation: false,
        timeline: false,
        skyBox: new Cesium.SkyBox({
            backgroundColor: Cesium.Color.BLACK
        })
    });
    return viewer;
}

// Plot position of sat on cesium map
function plot_positions(arr_lla, points) {
    points.removeAll(); // remove old points before update

    var i;

    for (i = 0; i < arr_lla.length; i++) {
        points.add({
            position: Cesium.Cartesian3.fromDegrees(arr_lla[i][0],
                              arr_lla[i][1], arr_lla[i][2]),
            pixelSize: 1.5,
            color: Cesium.Color.CYAN.withAlpha(0.5)
        });
    }
}

// Use satellite.js to read tle and return js array of lats and lons
function get_positions(tle) {
    let object_lla = [];
    let i = 0;
    for (let key of Object.keys(tle)) {
        let l1 = tle[key][0],
            l2 = tle[key][1];
        try {
            object_lla[i] = compute_position(l1, l2);
            i++;
        }
        catch(err) {
            //console.log("ERROR COMPUTING: ", key);
            //console.log("\tREASON: ", err);
        }
    }
    return object_lla;
}

// Use satellite.js to compute lat, lon, height from tle
function compute_position(l1, l2) {
    var satrec = satellite.twoline2satrec(l1, l2);
    var positionAndVelocity = satellite.propagate(satrec, new Date());
    var positionEci = positionAndVelocity.position,
        velocityEci = positionAndVelocity.velocity;
    var gmst = satellite.gstime(new Date());

    var positionGd = satellite.eciToGeodetic(positionEci, gmst);
    var longitude = positionGd.longitude,
        latitude = positionGd.latitude,
        height = positionGd.height * 1000;
    
    longitude = satellite.degreesLong(longitude);
    latitude = satellite.degreesLat(latitude);

    return [longitude, latitude, height];
}
