// // 定义一个函数来获取数据并更新表格
// async function fetchDataAndUpdateTable() {
//     try {
//         // 向接口发送 POST 请求获取数据
//         const response = await fetch('http://127.0.0.1:5000/post_select_data', {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json'
//             },
//             // 可选的请求体（如果有的话）
//             body: JSON.stringify({}) // 如果有额外的数据需要发送，请在这里添加
//         });
//
//         // 将响应数据解析为 JSON 格式
//         const data = await response.json();
//
//         // 获取表格的 tbody 元素
//         const tableBody = document.querySelector('#dataTable tbody');
//
//         // 清空表格内容
//         tableBody.innerHTML = '';
//
//         // 循环遍历数据，将每个条目添加到表格中
//         const row = `
//             <tr>
//                 <td>${data.id}</td>
//                 <td>${data.shidu}</td>
//                 <td>${data.wendu}</td>
//             </tr>
//         `;
//
//         // 将当前条目添加到表格中
//         tableBody.innerHTML += row;
//     } catch (error) {
//         console.error('Error fetching data:', error);
//     }
// }
//
// // 页面加载时立即调用函数开始获取数据并更新表格
// fetchDataAndUpdateTable();
//
// // 每10秒钟调用一次函数更新数据
// setInterval(fetchDataAndUpdateTable, 5000);

async function fetchDataAndUpdateTable() {
    try {
// 发送 POST 请求
        fetch('http://127.0.0.1:5000/post_select_data', {
            method: 'POST', // 指定请求方法为 POST
            headers: {
                'Content-Type': 'application/json' // 指定请求头的内容类型为 JSON 格式
            }
        })
            .then(response => response.json()) // 解析响应为 JSON 格式
            .then(data => {
                // 获取表格的 tbody 元素
                var tableBody = document.getElementById('dataBody');

                // 循环遍历 JSON 数据，生成表格内容
                data.forEach(function (item) {
                    var row = '<tr>';
                    row += '<td>' + item.id + '</td>';
                    row += '<td>' + (item.shidu === null ? 'null' : item.shidu) + '</td>';
                    row += '<td>' + item.wendu + '</td>';
                    row += '</tr>';
                    tableBody.innerHTML += row;
                });
            })
            .catch(error => console.error('Error:', error)); // 处理请求错误
    }catch (error) {
        console.error('Error fetching data:', error);
    }

}
// 页面加载时立即调用函数开始获取数据并更新表格
fetchDataAndUpdateTable();

// 每10秒钟调用一次函数更新数据
setInterval(fetchDataAndUpdateTable, 5000);