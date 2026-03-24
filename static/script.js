document.getElementById('loanForm').addEventListener('submit', function(e){
    e.preventDefault();

    const data = {
        income: parseFloat(document.getElementById('income').value),
        credit_score: parseFloat(document.getElementById('credit_score').value),
        loan_amount: parseFloat(document.getElementById('loan_amount').value),
        employment_years: parseFloat(document.getElementById('employment_years').value),
        debt_to_income: parseFloat(document.getElementById('debt_to_income').value)
    };

    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        document.getElementById('result').innerText = `Loan Status: ${result.loan_status}`;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
