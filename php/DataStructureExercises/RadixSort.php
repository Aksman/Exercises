<?php
/***
 * EXERCISE
 * Implement a Radix Sort in PHP
 */

namespace Aksman\Exercises\php\DataStructureExercises;

class RadixSort
{
    /**
     * Sorts an array of non-negative integers using a Radix Sort.
     * @param array $arr The array to be sorted.
     * @return void
     */
    public static function sort(array &$arr): void
    {
        if (empty($arr)) {
            return;
        }

        // Find the maximum number to know how many digits
        $max = max($arr);

        // Run a counting sort for every digit position.
        // $exp is a power of 10 representing the current digit number (i.e. 1, 10, 100, ...)
        for ($exp = 1; floor($max / $exp) > 0; $exp *= 10) {
            self::countingSort($arr, $exp);
        }
    }

    /**
     * Performs a stable counting sort on the array based on a specific digit position.
     * @param array $arr The array being sorted
     * @param int $exp The power of 10 representing the digit being sorted (i.e. 1, 10, 100, ...)
     * @return void
     */
    private static function countingSort(array &$arr, int $exp): void
    {
        $n = count($arr);
        $output = array_fill(0, $n, 0);
        $count = array_fill(0, 10, 0);

        // 1. Store the count of occurrences of each digit (0-9) at the current place value
        for ($i = 0; $i < $n; $i++) {
            $digit = floor($arr[$i] / $exp) % 10;
            $count[$digit]++;
        }

        // 2. Modify the count array so it contains actual positions in the output array
        // This transforms the counts into running totals, corresponding to the ending indexes
        // in the resulting array.
        for ($i = 1; $i < 10; $i++) {
            $count[$i] += $count[$i - 1];
        }

        // 3. Build the output array by placing elements in a stable manner (backward loop)
        // This is done to preserve order of equal elements.
        for ($i = $n - 1; $i >= 0; $i--) {
            $digit = floor($arr[$i] / $exp) % 10;
            $output[$count[$digit] - 1] = $arr[$i];
            $count[$digit]--;
        }

        // 4. Copy the sorted elements back into the original array
        for ($i = 0; $i < $n; $i++) {
            $arr[$i] = $output[$i];
        }
    }
}

if (get_included_files()[0] == __FILE__) {
    $data = [];
    for($i = 0; $i < 99; $i++) {
        $data[] = random_int(1, 1000);
    }

    echo "Original array: \n";
    echo implode(', ', $data) . "\n";

    RadixSort::sort($data);

    echo "Sorted array: \n";
    echo implode(', ', $data);
}