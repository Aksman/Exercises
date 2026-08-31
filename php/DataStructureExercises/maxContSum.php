<?php
/***
 * EXERCISE
 * Create a function that takes an array ofintegers and find that contiguous run with the largest sum.
 */

namespace Aksman\Exercises\php\DataStructureExercises;
use Random\Randomizer;

/**
 * Find the continguous slice of size $target with the largest sum. This function
 * is an example of the Sliding Window Algorithm.
 * @param int $length
 * @param array $list
 * @return array
 */
function maxContSum(int $length, array $list): array 
{
    // Zero and negative lengths are not allowed
    if ($length <= 0) {
        throw new \InvalidArgumentException('Length must be a positive integer.');
    }
    // Sanity check: if the array length is less than or equal to length, just return the array.
    if (count($list) <= $length) {
        return $list;
    }
    // Work with a sequential version of the list
    $vals = array_values($list);

    // Initialize with the sum at the beginning of the array.
    $current = array_sum(array_slice($vals, 0, $length));
    $max = $current;
    $maxOffset = 0;

    // Proceed through the list. 
    for($i = 1; $i < count($vals) - $length + 1; $i++) {
        // Note that instead of computing a fresh sum every time, we instead 
        // subtract the number which has moved out of our "window" and added the 
        // number which has moved in.
        $current += $vals[$i + $length - 1] - $vals[$i - 1];
        // If the sum of current slice is greater than the maximum,
        // set the new maximum and record the location.
        if ($current > $max) {
            $max = $current;
            $maxOffset = $i;
        }
    }

    // Return the slice of the array starting with $maxOffset, preserving keys.
    // Note the use of a PHP8 named parameter for preserve_keys for the sake of readability.
    return array_slice($list, $maxOffset, $length, preserve_keys: true);
}

if (get_included_files()[0] == __FILE__) {
    $keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];
    $random = new Randomizer();
    $list = [];
    foreach ($keys as $k) {
        $list[$k] = $random->getInt(1, 100);
    }

    echo "My List: ";
    foreach($list as $key => $val) {
        echo "{$key}:{$val} ";
    }
    echo "\n\n";
    $maxSlice = maxContSum(5, $list);
    echo "Maximum run: "; 
    foreach($maxSlice as $k => $v) {
        echo "{$k}:{$v} ";
    }
    echo "\n";
    echo "Sum: " . array_sum($maxSlice) . "\n";
}