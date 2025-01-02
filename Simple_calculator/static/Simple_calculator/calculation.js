document.addEventListener('DOMContentLoaded', function () {
    //ใช้ getElementById เพื่อเชื่อมกับตัวช่องใส่เลขและช่องคำตอบ
    const num1Input = document.getElementById('num1');
    const num2Input = document.getElementById('num2');
    const resultBox = document.getElementById('result-box');
    //ใช้ querySelectorAll เพื่อดีง element ของปุ่มทั้งหมด
    const operationButtons = document.querySelectorAll('.operation');

    const compute = (operation) => {
        //ดึงตัวเลขจากช่องใส่ตัวเลข
        const num1 = parseFloat(num1Input.value);
        const num2 = parseFloat(num2Input.value);
        let result = 0;
        //ใช้ swich case ในการเลื่อกการคำนวน
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
        //assign ผลลัพธ์ลงในช่องผลลัพธื
        resultBox.textContent = `${result}`;
    }
    //assign function ของแต่ละปุ่มให้เรียกใช้ compute และส่งตัวเลื่อกในการคำนวนเข้าไป
    operationButtons.forEach(button =>{
        button.addEventListener('click',function () {
            compute(button.value)
        })
    })
});