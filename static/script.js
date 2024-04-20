async function obtenerDatos() {
    const response = await fetch('http://localhost:8000/index');
    const data = await response.json();

    mostrarDatos(data);
}

function mostrarDatos(data) {
    const datosContainer = document.getElementById('datos-container');
    datosContainer.innerHTML = ''; // Limpiar el contenedor antes de agregar la tabla
    const tablaDatos = crearTablaDatos(data);
    datosContainer.appendChild(tablaDatos);
}

function crearTablaDatos(data) {
    const tabla = document.createElement('table');
    tabla.innerHTML = `
        <thead>
            <tr>
                <th>ID</th>
                <th>Paciente</th>
                <th>Médico</th>
                <th>Cantidad</th>
                <th>Medicamento</th>
                <th>Observación</th>
                <th>Fecha</th>
            </tr>
        </thead>
        <tbody>
            ${data.map(dato => `
                <tr>
                    <td>${dato.id_formula}</td>
                    <td>${dato.Paciente}</td>
                    <td>${dato.Medico}</td>
                    <td>${dato.Cantidad}</td>
                    <td>${dato.Medicamento}</td>
                    <td>${dato.Observacion}</td>
                    <td>${dato.Fecha}</td>
                </tr>
            `).join('')}
        </tbody>
    `;
    return tabla;
}

async function agregarDato() {
    const nuevoDato = {
        Paciente: prompt('Ingrese el nombre del paciente:'),
        Medico: prompt('Ingrese el nombre del médico:'),
        id_formula: prompt('Ingrese el ID de la formulación:'),
        Cantidad: prompt('Ingrese la cantidad:'),
        Medicamento: prompt('Ingrese el nombre del medicamento:'),
        Observacion: prompt('Ingrese alguna observación:'),
        Fecha: prompt('Ingrese la fecha (YYYY-MM-DD):')
    };

    const response = await fetch('http://localhost:8000/datos', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(nuevoDato)
    });

    if (response.ok) {
        const data = await response.json();
        mostrarDatos([data]); // Mostrar el nuevo dato en la tabla
    } else {
        console.error('Error al agregar el dato:', response.statusText);
    }
}

// Event listener para el botón de agregar dato
document.getElementById('agregar-dato').addEventListener('click', agregarDato);

// Event listener para el botón de obtener datos
document.getElementById('obtener-datos').addEventListener('click', obtenerDatos);
