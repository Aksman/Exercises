<?php
/**************
 * EXERCISE
 * Create a function that returns the factorial of a given integer.
 */
namespace Aksman\Exercises\php\MathExercises;
use InvalidArgumentException;

function factorial(int $num): int
{
    // Negative numbers do not have factorials.
    if ($num < 0) {
        throw new InvalidArgumentException('factorial() cannot accept a negative number');
    }
    // 0! and 1! are defined to be 1.
    if ($num == 0 || $num == 1) {
        return 1;
    }
    // Since we're multiplying, start with 1.
    $f = 1;
    for($i = 2; $i <= $num; $i++) {
        $f *= $i;
    }
    return $f;
}

// Run this block only if this script is run directly (not included).
if (get_included_files()[0] == __FILE__) {
    for ($i = 0; $i <= 10; $i++) {
        $f = factorial($i);
        echo "{$i}! = {$f}\n";
    }
}