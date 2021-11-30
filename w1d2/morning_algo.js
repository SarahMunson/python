// addToFront(arr, value)
// add a given value to the front of the array and return that array
// the arguments [1, 2, 3] and 4 result in the array [4, 1, 2, 3]

function addToFront(arr, value) {
    arr.length +=1;
    arr[4] = arr[3]
    arr[3] = arr[2]
    arr[2] = arr[1]
    arr[1] = arr[0]
    arr[0] = value
    console.log(arr)
}

// addToFront([1, 3, 5, 6], 5)

// a more general approach

function addToFront2(arr=[], value=0){
    arr.length += 1
    for(var i = arr.length-1; i > 0; i--){
        arr[i] = arr[i - 1];
    }
    arr[0] = value
    return arr
}

console.log(addToFront2([1, 3, 5], 7))
console.log(addToFront2([], 7))
console.log(addToFront2([]))
console.log(addToFront2([1, 3, 5]))


// removeFront(arr)
// remove the value from the front of the array and return that array
// [7, 1, 4, 9] as the argument should result in an output of [1, 4, 9]

function removeFront(arr) {
    if(arr.length < 1){
        return "Unacceptable!"
    }
    for(var i = 0; i < arr.length; i++){
        arr[i] = arr[i + 1];
    }
    arr.length -= 1
    return arr
}

console.log(removeFront([1, 4, 5, 7, 8]))
console.log(removeFront([1]))
console.log(removeFront([]))
