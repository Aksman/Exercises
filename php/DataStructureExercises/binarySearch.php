<?php
/***
 * EXERCISE
 * Implement a binary search in PHP.
 */

namespace Aksman\Exercises\php\DataStructureExercises;
use Random\Randomizer;

/**
 * Implementation of a binary search on a PHP array.
 * @param mixed $needle The value searched for.
 * @param array $haystack The array being searched.
 * @return mixed Return the key associated with the value, if found. Return null if not.
 */
function binarySearch(mixed $needle, array $haystack): mixed
{
    // Sort the array by value while presering key-value associations
    asort($haystack);

    // For this algorithm it's easier to work with sequential arrays. We will search the 
    // $vals array, then find the corresponding value in keys.
    $keys = array_keys($haystack);
    $vals = array_values($haystack);

    // Set pointers at the beginning and end of the array.
    $left = 0;
    $right = count($vals) - 1;

    // Run until the pointers meet... unless we find our needle.
    while($left < $right) {
        // Let our index be at the middle point between the $left and $right indexes.
        $mid = floor(($left + $right) / 2);
        // If we've found our value, return the corresponding key.
        if ($vals[$mid ] == $needle) {
            return $keys[$mid];
        // If less than our needle, let the index be our new left value and search again.
        } else if ($vals[$mid] < $needle) {
            $left = $mid;
        // If greater than, let the index be our new right value and search again.
        } else {
            $right = $mid;
        }
    }

    // If we've made in all the way through without finding our needle, return null to indicate not found.
    return null;
}

// Example usage
if (get_included_files()[0] == __FILE__) {
    $random = new Randomizer();
    $list = [];
    for ($i = 0; $i < 199; $i++) {
        $list[] = $random->getInt(1, 10000);
    }
    $insertAt = $random->getInt(0, 199);
    $target = $random->getInt(1, 10000);
    array_splice($list, $insertAt, 0, $target);

    echo "List: " . implode(', ', $list) . "\n";
    $lookup = binarySearch($target, $list);
    echo "Target \"{$target}\" found at index \"{$lookup}\".\n";

}