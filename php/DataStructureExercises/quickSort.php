<?php
/***
 * EXERCISE
 * Re-create a quick sort function.
 */

namespace Aksman\Exercises\php\DataStructureExercises;

/***
 * A quick sort is considered the best of the classic sorting algorithms. It selects on element from 
 * the array and then sorts the elements into three arrays: one for all elements less than the pivot, one for
 * those equal to the pivot, and one for those greater than it. From there, the function calls itself
 * recursively, sorting the lower-than and greater-than arrays in the same manner. The recursion stops
 * when an array has one element or less and no more sorting is necessary. The three partitions are then 
 * stitched back together to create a fully sorted array. 
 */
function quickSort(array $arr): array
{
    // If the array has one element or less, sorting is not necessary. We also need this stopping point 
    // to prevent infinite recursion.
    if (count($arr) <= 1) { 
        return $arr;
    }
    // Initialize our three partitions.
    $lower = [];
    $middle = [];
    $upper = [];
    // We use the first element as our pivot. We use PHP's array_first() function (introduces in v8.5)
    // as PHP arrays can be associative and the first element is not necessarily $array[0].
    $pivot = array_first($arr);
    // Put all key-value pairs in the corresponding partition based on a comparison with the pivot value.
    // Note that we are sorting by value but preserving the key association.
    foreach($arr as $key => $value) {
        if ($value < $pivot) {
            $lower[$key] = $value;
        } elseif ($value == $pivot) {
            $middle[$key] = $value;
        } else {
            $upper[$key] = $value;
        }
    }

    // Here is where the recusrion magic happens. We recusively call this very function on the $lower and 
    // $upper partitions. So those partitions will in turn be sorted into lower, middle, and upper partitions,
    // and this function will be called on those partitions as well. This will happen until we have partitions
    // that have 1 or 0 elements. At that point, we will have a sorted array.
    return quickSort($lower) + $middle + quickSort($upper);
}

// Run this block only if the script is run directly (i.e. not included).
if (get_included_files()[0] == __FILE__) {
    $myArray = [57, 69, 98, 61, 97,
                95,	68,	4,	49,	43,
                85,	66,	72,	92,	32,
                92,	21,	51,	53,	98,
                82,	13,	47,	13,	85,
    ];

    $sortedArray = quickSort($myArray);

    echo "SORTED ARRAY:\n";
    echo "=============\n";
    foreach($sortedArray as $key => $value) {
        echo "{$key}: {$value}\n";
    }
}