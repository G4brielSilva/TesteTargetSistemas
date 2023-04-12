const faturamentoMensal = [
    {
        estado: "SP",
        valor: 67836.43
    },
    {
        estado: "RJ",
        valor: 36678.66
    },
    {
        estado: "MG",
        valor: 29229.88
    },
    {
        estado: "ES",
        valor: 27165.48
    },
    {
        estado: "Outros",
        valor: 19849.53
    }
]

function getFaturamentoTotal(): number {
    let sum = 0;

    for (let faturamento of faturamentoMensal) {
        sum += faturamento.valor;
    }

    return sum;
}

function getPercentuais(faturamentoTotal: number) {
    let percentuais: object[] = [];

    for (let faturamento of faturamentoMensal) {

        let percentual = (faturamento.valor * 100)/faturamentoTotal;

        percentuais.push({
            estado: faturamento.estado,
            percentual: Math.round( 100 * percentual) / 100
        });
    }

    return percentuais;
}

let faturamentoTotal = getFaturamentoTotal();
console.log(getPercentuais(faturamentoTotal));