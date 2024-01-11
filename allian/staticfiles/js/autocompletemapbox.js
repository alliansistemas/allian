const mytoken = "pk.eyJ1IjoicnVhbm1vcmFlczAxOCIsImEiOiJjbGxvM2prZGgwNWl1M2VrdTlwdmkwbGFlIn0.9PbfTFPMl2qRGr8Zx31j3Q";
    const MAPBOX_BASE = 'https://api.mapbox.com/geocoding/v5/mapbox.places/';

    // Autocomplete para Origem
    new Autocomplete('#autocompleteOrigem', {
        search: input => {
            const url = `${MAPBOX_BASE}${encodeURIComponent(input)}.json?access_token=${mytoken}&limit=5&language=pt-BR`;
            return new Promise(resolve => {
                fetch(url)
                    .then(response => response.json())
                    .then(data => {
                        resolve(data.features)
                    })
            })
        },
        renderResult: (result, props) => {
            result = result.place_name;
            let group = '';
            if (result.index % 3 === 0) {
                group = `<li class="group">Group</li>`
            }
            return `
        ${group}
        <li ${props}>
            <div class="wiki-title">
                ${result}
            </div>
        </li>
        `
        },
        getResultValue: result => result.place_name,
        onSubmit: result => {
            console.log("Origem latitude", result.geometry.coordinates[0])
            console.log("Origem longtitude", result.geometry.coordinates[1])
            console.log("Origem Place Name", result.place_name)
        }
    });

    // Autocomplete para Destino
    new Autocomplete('#autocompleteDestino', {
        search: input => {
            const url = `${MAPBOX_BASE}${encodeURIComponent(input)}.json?access_token=${mytoken}&limit=5&language=pt-BR`;
            return new Promise(resolve => {
                fetch(url)
                    .then(response => response.json())
                    .then(data => {
                        resolve(data.features)
                    })
            })
        },
        renderResult: (result, props) => {
            result = result.place_name;
            let group = '';
            if (result.index % 3 === 0) {
                group = `<li class="group">Group</li>`
            }
            return `
        ${group}
        <li ${props}>
            <div class="wiki-title">
                ${result}
            </div>
        </li>
        `
        },
        getResultValue: result => result.place_name,
        onSubmit: result => {
            console.log("Destino latitude", result.geometry.coordinates[0])
            console.log("Destino longtitude", result.geometry.coordinates[1])
            console.log("Destino Place Name", result.place_name)
        }
    });