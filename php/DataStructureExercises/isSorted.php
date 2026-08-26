<?php
/***
 * Create a function that determines if an array is sorted.
 */

namespace Aksman\Exercises\php\DataStructureExercises;

/**
 * Summary of Aksman\Exercises\php\DataStructureExercises\isSorted
 * @param array $arr The array being examined
 * @param bool $descending Flag if we are expecting descending order (default false).
 * @return bool true if the array is sorted, false if not.
 */
function isSorted(array $arr, bool $descending=false): bool
{
    $prev = null;
    foreach($arr as $el) {
        if ($prev !== null) {
            if ($descending) {
                if ($prev < $el) {
                    return false;
                }
            } else {
                if ($prev > $el) {
                    return false;
                }
            }
        }
        $prev = $el;
    }
    return true;
}

// EXAMPLE USAGE
// This block only runs if this script is run directly.
if (get_included_files()[0] == __FILE__) {
    $arrs = [
        1 => [1, 2, 3, 4, 5, 6, 7],
        2 => [1, 2, 3, 7, 4, 6, 5],
        3 => ['Avery Anderson', 'Brian Bates', 'Christina Calloway', 'David Denton', 'Ellie Edwards', 'Fred Fisher'],
        4 => ['A', 'B', 'D', 'C', 'B', 'C'],
        5 => [8, 7, 6, 5, 4, 3],
    ];

    foreach($arrs as $k => $arr) {
        if ($k == 5) {
            $isSorted = (isSorted($arr, true)) ? '' : 'not ';
        } else {
            $isSorted = (isSorted($arr)) ? '' : 'not ';
        }
        echo "Array #{$k} is {$isSorted}sorted.\n";
    }
}