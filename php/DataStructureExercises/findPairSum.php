<?php
/***
 * EXERCISE
 * Create a function that takes an array of numbers and returns a pair whose sum totals a target value.
 */

namespace Aksman\Exercises\php\DataStructureExercises;
use Random\Randomizer;

/**
 * Find a pair of two numbers in a list whose sum equals the target. This is an implementation
 * of the two pointers algorithm.
 * @param int $target
 * @param array $numberList
 * @return array|null
 */
// Preceding the return type with a "?" means we're allowed to return null instead.
function findPairSum(int $target, array $numberList): ?array 
{
    // Sort the array
    sort($numberList);

    // Set the left and right pointers to the beginning and end of the list.
    $left = 0;
    $right = count($numberList) - 1;

    // The $left and $right pointers will move inward until we find a pair with 
    // the target sum or they pointers meet.
    while($left < $right) {
        $currentSum = $numberList[$left] + $numberList[$right];
        // If we've found our target pair, stop.
        if ($currentSum == $target) {
            break;
        // If the sum is less than the target, move the left pointer forward.
        } else if ($currentSum < $target) {
            $left++;
        // If the sum is greater than the target, move the right pointer backward.
        } else {
            $right--;
        }
    }

    // Verify the left and right pointers found the target sum, and that the loop did not 
    // end because they met. If so, return an array with the two numbers.
    if ($numberList[$left] + $numberList[$right] == $target) {
        return [$numberList[$left], $numberList[$right]];
    } else {
        return null;
    }
}

// Example usage
// This block only runs if the script is run directly, i.e. is not included.
if (get_included_files()[0] == __FILE__) {
    $random = new Randomizer();
    $numbers = [];
    for ($i = 0; $i < 25; $i++) {
        $numbers[] = $random->getInt(1, 100);
    }

    $target = $random->getInt(50, 150);

    echo "Numbers: " . implode(', ', $numbers) . "\n";
    echo "Target Sum: " . $target . "\n";
    $addends = findPairSum($target, $numbers);
    if ($addends) {
        echo "Pair found: {$addends[0]} + {$addends[1]}\n";
    } else {
        echo "Pair not found.\n";
    }
}