const data = {
    1: {id: 1, pid: 0, name: 'aa'},
    2: {id: 2, pid: 0, name: 'bb'},
    3: {id: 3, pid: 0, name: 'cc'},
    4: {id: 4, pid: 3, name: 'dd'},
    5: {id: 5, pid: 4, name: 'ee'},
    6: {id: 6, pid: 3, name: 'ff'},
    7: {id: 7, pid: 1, name: 'gg'},
    8: {id: 8, pid: 5, name: 'hh'},
    9: {id: 9, pid: 6, name: 'ii'},
    10: {id: 10, pid: 8, name: 'jj'},
    11: {id: 11, pid: 7, name: 'kk'},
};

function genTree(srcData) {
    // 简单的深复制
    var data = JSON.parse(JSON.stringify(srcData));
    let tree = [];

    for (var i in data) {
        var item = data[i];
        if (data[item.pid]) {
            !!data[item.pid].child || (data[item.pid].child = []);
            data[item.pid].child.push(item);
        } else {
            tree.push(data[item.id]);
        }
    }

    return tree;
}

const tree = genTree(data);

console.log(tree);
console.log(data);