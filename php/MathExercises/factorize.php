<?php
/***
 * EXERCISE
 * Create a function that finds the factors of a positive integer
 */

namespace Aksman\Exercises\php\MathExercises;

/**
 * Find all the factors of a positive integer.
 * @param int $number
 * @throws \InvalidArgumentException
 * @return array
 */
function factorize(int $number): array 
{
    if ($number <= 0) {
        throw new \InvalidArgumentException('Must be a positive integer.');
    }
    if ($number == 1) {
        return [1];
    }
    // $factorFlags is an associative array which contains all natural number up to the input number.
    // We initialize them all to false, then mark true as we find factors.
    $factorFlags = array_fill(1, $number, false);
    // Mark 1 and the number as factors.
    $factorFlags[1] = true;
    $factorFlags[$number] = true;

    // The upper bound is designed to be revised downward as we find factors. Every time we find a factor
    // we find the other factor it corresponds to it. There will not be any factors larger than it that we
    // have not already found, so we revise the stopping point downward.
    $upperBound = $number;
    for($i = 2; $i < $upperBound; $i++) {
        if (!$factorFlags[$i]) {
            if ($number % $i == 0) {
                $factorFlags[$i] = true;
                $upperBound = $number / $i;
                $factorFlags[$upperBound] = true;
            }
        }
    }
    return array_keys(array_filter($factorFlags, fn($n) => $n));
}

if (get_included_files()[0] == __FILE__) {
    $number = (int)($argv[1] ?? 72);

    $factors = factorize($number);
    echo implode(', ', $factors);
}