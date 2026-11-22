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


const options = ["AREY SUB PS",
"AGRIPADA",
"AIR PORT",
"ANDHERI",
"AZAD MAIDAN",
"BANDRA",
"BHANDUP",
"BHOIWADA",
"BORIWALI",
"BYCULLA",
"CHEMBUR",
"COLABA",
"DADAR",
"DHARAVI",
"DONGRI",
"GAMDEVI",
"GHATKOPAR",
"GOREGAON",
"JOGESHWARI",
"KALACHOWKI",
"KANDIVALI (WEST)",
"KHERWADI",
"KURLA",
"D.B.MARG",
"LT MARG",
"MAHIM",
"MALAD",
"MATUNGA",
"MULUND (WEST)",
"NAGPADA",
"NM JOSHI MARG",
"M R A MARG",
"PYDHONIE",
"SANTACRUZ",
"SEWRI",
"TILAK NAGAR",
"VIKHROLI",
"VILE PARLE",
"V.P.ROAD",
"WADALA",
"WORLI",
"YELLOWGATE",
"VAKOLA",
"TROMBAY",
"MALVANI",
"SAKINAKA",
"DAHISAR",
"D.N.NAGAR",
"R.A KIDWAI MARG",
"TARDEO",
"SAHAR",
"ANTOP HILL",
"DEONAR",
"JUHU",
"KANJUR MARG",
"NIRMAL NAGAR",
"MIDC",
"KASTURBA SUB PS",
"NEHRU NAGAR",
"R C F",
"PANT NAGAR",
"DINDOSHI",
"KHAR",
"CUFFE-PARADE",
"OSHIWARA",
"PARK SITE",
"SHIVAJI NAGAR",
"SIR JJ MARG",
"SHIVAJI PARK",
"MALABAR HILL",
"MEGHWADI",
"SION",
"KURAR",
"MHB COLONY",
"NAVGHAR",
"SHAHU NAGAR",
"VERSOVA",
"MARINE DRIVE",
"WADALA TT",
"BANDRA-KURLA COMPLEX",
"POWAI",
"CHARCOP",
"VINOBA BHAVE NAGAR",
"GORAI",
"BANGUR NAGAR",
"SAMTA NAGAR",
"Mumbai Sagri Police Station",
"GOVANDI POLICE STATION",
"MANKHURD POLICE STATION",
"CHUNABHATTI POLICE STATION",
"AMBOLI",
"VANRAI POLICE STATION",
"Mumbai Sagri-2 Police Station",
"CYBER POLICE STATION WEST REGION",
"CYBER POLICE STATION EAST REGION",
"CYBER POLICE STATION CENTRAL REGION",
"CYBER POLICE STATION NORTH REGION",
"CYBER POLICE STATION SOUTH REGION"]


const search = document.getElementById("search");
const dropdown = document.getElementById("dropdown");

search.addEventListener("input", function () {
    const query = search.value.toLowerCase();

    dropdown.innerHTML = "";

    if (query.length === 0) {
        dropdown.style.display = "none";
        return;
    }

    const filtered = options.filter(option =>
        option.toLowerCase().includes(query)
    );

    filtered.forEach(option => {
        const item = document.createElement("div");

        item.className = "dropdown-item";
        item.textContent = option;

        item.addEventListener("click", function () {
            search.value = option;
            window.open(`/crime/reviews/search/?q=${encodeURIComponent(option)}`, '_blank', 'noopener,noreferrer');
            
        });

        dropdown.appendChild(item);
    });

    dropdown.style.display =
        filtered.length > 0 ? "block" : "none";
});