const data = {
    1: {id: 1, pid: 0, name: 'aa'},
    2: {id: 2, pid: 0, name: 'bb'},
    3: {id: 3, pid: 0, name: 'cc'},
    4: {id: 4, pid: 3, name: 'dd'},
    5: {id: 5, pid: 4, name: 'ee'},
    6: {id: 6, pid: 3, name: 'ff'},
    7: {id: 7, pid: 4, name: 'gg'},
    8: {id: 8, pid: 5, name: 'hh'},
    9: {id: 9, pid: 6, name: 'ii'},
    10: {id: 10, pid: 8, name: 'jj'},
    11: {id: 11, pid: 7, name: 'kk'},
};

function genTree(data) {
    let tree = {
        id: 0,
        name: 'root',
        child: {},
    };

    data.forEach((item) => {
    });
}