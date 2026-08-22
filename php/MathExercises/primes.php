<?php
/***
* EXERCISE
* Create a function to produce a sequential array of all the prime numbers 
* less than or equal to a specified value.
*/

namespace Aksman\Exercises\php\MathExercises;

function primes(int $upper): array
{
    // Create an array associating the numbers 2 to $upper with a boolean value. a
    // Initialize all of them to true.
    // array_fill_keys() creates an associative array with an array of keys all set to 
    // a speficied value. 
    $numbers = array_fill_keys(range(2, $upper), true);
    // We loop through all the numbers from 2 to the square root of our $upper value.
    for($i = 2; $i < sqrt($upper); $i++) {
        // For every number we find associated with a true value, we keep it as true, 
        // then set all of its multiples to false. As we progress sequentially, every 
        // subsequent number set to true will be prime, but we will need to set all 
        // its multiples to false. We can stop at sqrt($upper) because at that point
        // we've found all the composites in the range.
        if ($numbers[$i]) {
            for($j = $i * 2; $j <= $upper; $j += $i) {
                $numbers[$j] = false;
            }
        }
    }
    // array_filter() filters the items in the array (key and value), keeping the items
    // where the function is equal to true. "fn($v) => $v" is an arrow function
    // (introduced in PHP 7.4), a shorthand way of defining a function. This function simply 
    // returns the value, which in this case is true of false. array_keys() returns an array containing
    // all the keys in the array returned by array_filter().
    return array_keys(array_filter($numbers, fn($v) => $v));
}

// Run this block only if the script is being run directly (i.e. not included).
if (get_included_files()[0] == __FILE__) {
    $primes = primes(100);
    $strListOfPrimes = implode(', ', $primes);
    echo "[{$strListOfPrimes}]";
}