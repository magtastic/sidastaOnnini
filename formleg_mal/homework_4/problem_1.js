var fs = require('fs');

// READ DATA CODE
const DATA_FILE = 'dist1.txt';

function readFile() {
    return fs.readFileSync(DATA_FILE, 'utf8', function(err, data) {
        if (err) {
            console.log(err);
        }
        return data;
    });
}

function getData() { 
  const file = readFile();
  const result = file.split('\n');
  result
    .forEach((distanceNode, y) => {
      result[y] = distanceNode.split(' ');
      result[y] = result[y].filter(elem => elem !== '') 
      result[y] = result[y].map((elem) => parseInt(elem))
    });
  return result.filter(row => row.length !== 0);
}

// PROBLEM 1
function problem1() {
  const distanceNodes = getData();
  let totalLength = 0;

  distanceNodes.forEach((distanceNode, index) => {
    if (index === distanceNodes.length - 1) {
      return totalLength;
    }
    totalLength += distanceNode[index+1];
  });
  totalLength += distanceNodes[0][distanceNodes.length-1];
  return totalLength;
}

// PROBLEM 2
function removeNode(nodeA, nodes) {
  return nodes.filter((node) => node != nodeA);
}

function getRandomNode(nodes) {
  return nodes[getRandomIntFromXtoY(0,nodes.length-1)];
}

function getRandomIntFromXtoY(x, y) {
  return Math.floor(Math.random() * (y - x + 1)) + x;
}

function getLengthFromAtoB(nodeA, nodeB) {
  return nodeA.lengths[nodeB.index];
}

function getRandomLength() {
  const distanceNodes = getData();
  let nodesWhitCheckedBoolean = distanceNodes.map((distanceNode, index) => {
    return { lengths: distanceNode, checked: false, index };
  });

  let nodeA = getRandomNode(nodesWhitCheckedBoolean);
  const firstNode = {
    length: nodeA.lengths,
    checked: nodeA.checked,
    index: nodeA.index,
  }
  let nodeB;
  nodesWhitCheckedBoolean = removeNode(nodeA, nodesWhitCheckedBoolean);
  let totalLength = 0;
  while (nodesWhitCheckedBoolean.length !== 0) {
    let nodeB = getRandomNode(nodesWhitCheckedBoolean);
    nodesWhitCheckedBoolean = removeNode(nodeB, nodesWhitCheckedBoolean);

    totalLength += getLengthFromAtoB(nodeA, nodeB);
    nodeA = nodeB;
  }
  totalLength += getLengthFromAtoB(nodeA, firstNode);
  return totalLength;
}

function problem2() {
  const lengths = [];
  for (let i = 0; i <= 50; i++) {
    lengths.push(getRandomLength());
  }
  return lengths;
}

// PROBLEM 3
function getLengthFromAtoBNode(nodeA, nodeB) {
  return nodeA.lengths[nodeB.index].length;
}

function markNodeAsChecked(index, nodes) {
  nodes.forEach((node) =>  {
    node.lengths[index] = {
      length: node.lengths[index].length,
      checked: true
    }});
  return nodes;
}

function getNodeWithIndex(index, nodes) {
  for (let i = 0; i < nodes.length; i++) {
    if (nodes[i].index === index) {
      return nodes[i];
    }
  }
  return -1;
}

function indexOfMinLengthThatIsNotViseted(nodeA, nodes) {
  const { lengths } = nodeA;
  let min = Infinity;
  let minIndex;

  lengths.forEach((lengthObj, index) => {
    if (lengthObj.length < min
      && !lengthObj.checked
      && index !== nodeA.index) {
      min = lengthObj.length;
      minIndex = index;
    }
  });

  return minIndex;
}

function findNearestNode(nodeA, nodes) {
  const minIndex = indexOfMinLengthThatIsNotViseted(nodeA, nodes);
  return getNodeWithIndex(minIndex, nodes);
}

function problem3() {
  const distanceNodes = getData();
  let nodesWhitCheckedBoolean = distanceNodes.map((distanceNode, index) => {
    return { lengths: distanceNode, checked: false, index };
  });
  nodesWhitCheckedBoolean.forEach((node) => {
    node.lengths = node.lengths.map((length) => { 
      return { length, checked: false };
    });
  })

  const path = [];
  let firstNode = nodesWhitCheckedBoolean[0]; 
  path.push(0);
  let nodeA = nodesWhitCheckedBoolean[0];
  nodesWhitCheckedBoolean = removeNode(nodeA, nodesWhitCheckedBoolean)
  nodesWhitCheckedBoolean = markNodeAsChecked(0, nodesWhitCheckedBoolean)
  let totalLength = 0
  while (nodesWhitCheckedBoolean.length !== 0) {
    let nodeB = findNearestNode(nodeA, nodesWhitCheckedBoolean);
    path.push(nodeB.index);
    nodesWhitCheckedBoolean = removeNode(nodeB, nodesWhitCheckedBoolean);
    nodesWhitCheckedBoolean = markNodeAsChecked(nodeB.index, nodesWhitCheckedBoolean);

    totalLength += getLengthFromAtoBNode(nodeA, nodeB);
    nodeA = nodeB;
  }
  path.push(0);
  totalLength += getLengthFromAtoBNode(nodeA, firstNode);
  return { totalLength, path };
}

function calculateLengthOfPath(path, nodes) {
  let totalLength = 0;
  let nodeIndexA = path[0]
  let nodeIndexB = 0;
  for (let i = 1; i < path.length; i++) {
    nodeIndexB = path[i];
    totalLength += nodes[nodeIndexA][nodeIndexB];
    nodeIndexA = nodeIndexB;
  }
  totalLength += nodes[path[path.length -1]][path[0]];
  return totalLength;
}

function problem4() {
  let { totalLength, path } = problem3();
  let minLength = totalLength;
  const nodes = getData();
  let count = 0;
  while (true) {
    let oldPath = path.splice();
    for (let x = 0; x < path.length; x++) {
      for (let y = 0; y < path.length; y++) {
        path.swapItems(x,y);
        let newLength = calculateLengthOfPath(path, nodes);
        if (newLength < minLength) {
          console.log('found better path');
          minLength = newLength;
          count = 0;
          break;
        } else {
          count ++;
        }
        path = oldPath.splice();
      }
    }
    if ( count > 10000) {
      console.log(count);
      break;
    }
  }
  console.log(minLength, totalLength);
}

Array.prototype.swapItems = function(a, b){
  this[a] = this.splice(b, 1, this[a])[0];
  return this;
}

problem4();
