document.addEventListener('DOMContentLoaded', function () {
    const num1Input = document.getElementById('num1');
    const num2Input = document.getElementById('num2');
    const resultBox = document.getElementById('result-box');
    const operationButtons = document.querySelectorAll('.operation');

    const compute = (operation) => {
        const num1 = parseFloat(num1Input.value);
        const num2 = parseFloat(num2Input.value);
        let result = 0;

        switch (operation){
            case 'add':
                result = num1 + num2;
                break;
            case 'subtract':
                result = num1 - num2;
                break;
            case 'multiply':
                result = num1 * num2;
                break;
            case 'divide':
                if (num2 !== 0) {
                    result = num1 / num2;
                } else {
                    resultBox.textContent = 'Cannot divide by zero';
                    return;
                }
                break;
        }
        resultBox.textContent = `Result: ${result}`;
    }
    operationButtons.forEach(button =>{
        button.addEventListener('click',function () {
            compute(button.value)
        })
    })
});