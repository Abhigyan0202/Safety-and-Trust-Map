L.TileLayer.prototype.options.referrerPolicy = 'strict-origin-when-cross-origin';

        const map = L.map("map").setView(
            [19.0760, 72.8777],
            11
        );

        L.tileLayer(
            "https://tile.openstreetmap.org/{z}/{x}/{y}.png",
            {
                maxZoom: 19,
                attribution:
                    '&copy; <a href="https://www.openstreetmap.org/copyright">' +
                    'OpenStreetMap</a> contributors'
            }
        ).addTo(map);
        const geojsonUrl =
    '/static/crime_data/mumbai_police_station_jurisdictions_matched.geojson';
    const coloursURL = "/getColours"

    const getRegionColour = async (region_name) => {
        return "#ff3300";
    }

    Promise.all([
    fetch('/static/crime_data/mumbai_police_station_jurisdictions_matched.geojson')
        .then(response => response.json()),

    fetch('/crime/getColours')
        .then(response => response.json())
])
.then(([geojsonData, colours]) => {
    //console.log(colours)
    const stations = L.geoJSON(geojsonData, {
        style: function(feature) {
            const regionName = feature.properties.name;
            return {
                color: '#333333',
                weight: 1,
                fillColor: colours[regionName][0] || '#cccccc',
                fillOpacity: 0.65
            };
        },

        onEachFeature: function(feature, layer) {

            const regionName = feature.properties.name;

            layer.bindTooltip(regionName + ` <br>AVG Rating - ${colours[regionName][1]}`);

            layer.on('click', (feature, layer)=> {
            //console.log(regionName);
            window.open(`/crime/reviews/search/?q=${encodeURIComponent(regionName)}`, '_blank', 'noopener,noreferrer');
});
        }

    }).addTo(map);

    map.fitBounds(stations.getBounds());

})
.catch(error => {
    console.error("Error loading map:", error);
});


