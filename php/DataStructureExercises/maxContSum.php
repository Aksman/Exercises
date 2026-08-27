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
 * @param int $target
 * @param array $list
 * @return array
 */
function maxContSum(int $target, array $list): array 
{
    // Make sure the list is sequentially indexed.
    $list = array_values($list);

    // Initialize with the sum at the beginning of the array.
    $current = array_sum(array_slice($list, 0, $target));
    $max = $current;
    $maxOffset = 0;

    // Proceed through the list. 
    for($i = 1; $i < count($list) - $target + 1; $i++) {
        // Note that instead of computing a fresh sum every time, we instead 
        // subtract the number which has moved out of our "window" and added the 
        // number which has moved in.
        $current = $current - $list[$i - 1] + $list[$i + $target - 1];
        // If the sum of current slice is greater than the maximum,
        // set the new maximum and record the location.
        if ($current > $max) {
            $max = $current;
            $maxOffset = $i;
        }
    }

    // Return the array slice based on the recorded location of the maximum sum.
    return array_slice($list, $maxOffset, $target);
}

if (get_included_files()[0] == __FILE__) {
    $random = new Randomizer();
    $list = [];
    for ($i = 0; $i < 25; $i++) {
        $list[] = $random->getInt(1, 100);
    }

    echo "My List: " . implode(', ', $list) . "\n";
    $maxSlice = maxContSum(5, $list);
    echo "Maximum run: " . implode(', ', $maxSlice) . "\n";
    echo "Sum: " . array_sum($maxSlice) . "\n";
}