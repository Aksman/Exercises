<?php
/***
 * EXERCISE
 * Implement a Timsort in PHP.
 */

namespace Aksman\Exercises\php\DataStructureExercises;


class Timsort 
{
    private const MIN_RUN = 32;

    /**
     * Sorts an array in-place using the Timsort algorithm.
     */
    public static function sort(array &$arr): void 
    {
        $n = count($arr);

        // Step 1: Sort individual sub-arrays of size MIN_RUN using Insertion Sort
        for ($i = 0; $i < $n; $i += self::MIN_RUN) {
            $left = $i;
            $right = min(($i + self::MIN_RUN - 1), ($n - 1));
            self::insertionSort($arr, $left, $right);
        }

        // Step 2: Merge the sorted runs sequentially
        $size = self::MIN_RUN;
        while ($size < $n) {
            for ($left = 0; $left < $n; $left += 2 * $size) {
                $mid = min(($left + $size - 1), ($n - 1));
                $right = min(($left + 2 * $size - 1), ($n - 1));

                // Only merge if there is a valid second run to merge with
                if ($mid < $right) {
                    self::merge($arr, $left, $mid, $right);
                }
            }
            $size *= 2;
        }
    }

    /**
     * In-place Insertion Sort for small slices/runs.
     */
    private static function insertionSort(array &$arr, int $left, int $right): void 
    {
        for ($i = $left + 1; $i <= $right; $i++) {
            $key = $arr[$i];
            $j = $i - 1;

            while ($j >= $left && $arr[$j] > $key) {
                $arr[$j + 1] = $arr[$j];
                $j--;
            }
            $arr[$j + 1] = $key;
        }
    }

    /**
     * Merges two sorted sub-arrays: $arr[$left..$mid] and $arr[$mid+1..$right]
     */
    private static function merge(array &$arr, int $left, int $mid, int $right): void 
    {
        // Slice the array out to simulate sub-arrays
        $leftArr = array_slice($arr, $left, $mid - $left + 1);
        $rightArr = array_slice($arr, $mid + 1, $right - $mid);

        $len1 = count($leftArr);
        $len2 = count($rightArr);

        $i = 0; // Initial index of first sub-array
        $j = 0; // Initial index of second sub-array
        $k = $left; // Initial index of merged array

        // Move smaller items back into the original array
        while ($i < $len1 && $j < $len2) {
            if ($leftArr[$i] <= $rightArr[$j]) {
                $arr[$k] = $leftArr[$i];
                $i++;
            } else {
                $arr[$k] = $rightArr[$j];
                $j++;
            }
            $k++;
        }

        // Copy any remaining elements of leftArr
        while ($i < $len1) {
            $arr[$k] = $leftArr[$i];
            $i++;
            $k++;
        }

        // Copy any remaining elements of rightArr
        while ($j < $len2) {
            $arr[$k] = $rightArr[$j];
            $j++;
            $k++;
        }
    }
}

// Example usage
// The following block is only run if this script is run directly (i.e. not included).
if (get_included_files()[0] == __FILE__) {
    $data = [];
    for($i = 0; $i < 155; $i++) {
        $data[] = random_int(-100, 1000);
    }

    echo "Original array: \n";
    echo implode(', ', $data);

    Timsort::sort($data);

    echo "Sorted array: \n";
    echo implode(', ', $data);
}