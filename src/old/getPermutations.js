function getPermutations(length) {
    const inputArr = [];
    for (let i = 1; i < length; i++) {
        inputArr.push(i);
    }
    // Generate all permutations
    var results = [];

    function permute(arr, memo) {
        var cur, memo = memo || [];

        for (var i = 0; i < arr.length; i++) {
            cur = arr.splice(i, 1);
            if (arr.length === 0) {
                results.push(memo.concat(cur));
            }
            permute(arr.slice(), memo.concat(cur));
            arr.splice(i, 0, cur[0]);
        }
        return results;
    }

    return permute(inputArr);
}

exports.getPermutations = getPermutations;
