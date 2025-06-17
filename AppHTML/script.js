const atributos = ['FOR', 'DES', 'CON', 'INT', 'SAB', 'CAR'];

window.onload = function() {
    const div = document.getElementById('atributos');
    atributos.forEach(attr => {
        div.innerHTML += `
            <div>
                <label>${attr}:</label>
                <input type="number" id="${attr}" value="10" min="1" max="20">
            </div>
        `;
    });
};

const subracas = {
    'Humano': ['Padrão'],
    'Elfo': ['Alto', 'Florestal', 'Negro'],
    'Anão': ['Da Colina', 'Da Montanha'],
    'Meio-Orc': ['Comum']
};

function atualizarSubracas() {
    const raca = document.getElementById('raca').value;
    const sub = document.getElementById('subraca');
    sub.innerHTML = '';
    subracas[raca].forEach(s => {
        sub.innerHTML += `<option>${s}</option>`;
    });
}

function mod(valor) {
    return Math.floor((valor - 10) / 2);
}

function gerarFicha() {
    const nome = document.getElementById('nome').value;
    const raca = document.getElementById('raca').value;
    const subraca = document.getElementById('subraca').value;
    const classe = document.getElementById('classe').value;

    let atr = {};
    atributos.forEach(attr => {
        atr[attr] = parseInt(document.getElementById(attr).value);
    });

    // Bônus raciais simples
    if (raca === 'Humano') {
        for (let a in atr) atr[a] += 1;
    } else if (raca === 'Elfo') {
        atr.DES += 2;
    } else if (raca === 'Anão') {
        atr.CON += 2;
    } else if (raca === 'Meio-Orc') {
        atr.FOR += 2;
    }

    // Vida por classe
    const vidaPorClasse = {
        'Guerreiro': 10,
        'Mago': 6,
        'Ladino': 8,
        'Clérigo': 8
    };

    const vida = vidaPorClasse[classe] + mod(atr.CON);

    let resultado = `📜 Ficha de ${nome}\n`;
    resultado += `Raça: ${raca} (${subraca})\n`;
    resultado += `Classe: ${classe}\n`;
    resultado += `Vida: ${vida}\n\n`;

    resultado += `🎯 Atributos:\n`;
    atributos.forEach(attr => {
        resultado += `${attr}: ${atr[attr]} (mod: ${mod(atr[attr])})\n`;
    });

    document.getElementById('resultado').innerText = resultado;
}
