<?php
/***
 * EXERCISE
 * Create a class that handles adding, subtracting, multiplying, and dividing with the DateInterval class.
 */

namespace Aksman\Exercises\php\MathExercises;
use DateInterval;
use DateTimeImmutable;

class DateIntervalMath
{
    /**
     * Add together two or more DateInterval objects.
     * @param DateInterval[] $intervals A list of DateInterval objects to be added together
     * @return DateInterval Returns their sum as a DateInterval object.
     */
    public static function add(DateInterval ...$intervals): DateInterval
    {
        $reference = new DateTimeImmutable('1970-01-01 00:00:00');
        $offsetTime = clone $reference;
        foreach($intervals as $interval) {
            $offsetTime = $offsetTime->add($interval);
        }
        return $reference->diff($offsetTime);
    }

    /**
     * Subtract one DateInterval object from another.
     * @param DateInterval $minuend The DateInterval object to start with.
     * @param DateInterval $subtrahend The DateInterval object to subtract.
     * @return DateInterval The result as a DateInterval object.
     */
    public static function subtract(DateInterval $minuend, DateInterval $subtrahend): DateInterval
    {
        $reference = new DateTimeImmutable('1970-01-01 00:00:00');
        $offsetTime = clone $reference;
        $offsetTime = $offsetTime->add($minuend)->sub($subtrahend);
        return $reference->diff($offsetTime);

    }

    /**
     * Multiply a DateInterval by a numerical value.
     * @param DateInterval $interval Representing the base date-time interval
     * @param int|float $factor The numerical factor to multiply by.
     * @return DateInterval The result
     */
    public static function multiply(DateInterval $interval, int|float $factor): DateInterval
    {
        $seconds = self::diToSeconds($interval);
        $seconds *= $factor;
        $rawInterval = DateInterval::createFromDateString("{$seconds} seconds");
        return self::normalizeDI($rawInterval);
    }

    /**
     * Divide a DateInterval by a numerical value.
     * @param DateInterval $interval
     * @param int|float $divisor
     * @return DateInterval
     */
    public static function divide(DateInterval $interval, int|float $divisor): DateInterval
    {
        $seconds = self::diToSeconds($interval);
        $seconds /= $divisor;
        $rawInterval = DateInterval::createFromDateString("{$seconds} seconds");
        return self::normalizeDI($rawInterval);
    }

    /**
     * A private helper function to convert a DateInterval object to seconds.
     * @param DateInterval $interval
     * @return int
     */
    private static function diToSeconds(DateInterval $interval): int
    {
        $reference = new DateTimeImmutable('1970-01-01 00:00:00');
        $offsetTime = $reference->add($interval);
        return $offsetTime->getTimestamp() - $reference->getTimestamp();
    }

    /**
     * A private helpter function to "normalize" a DateInterval object, so that then formatted
     * it shows a number of days, hours, minutes, and seconds.
     * @param DateInterval $interval
     * @return DateInterval
     */
    private static function normalizeDI(DateInterval $interval): DateInterval
    {
        $reference = new DateTimeImmutable('1970-01-01');
        $offsetTime = $reference->add($interval);
        return $offsetTime->diff($reference);
    }
}

// Example usage
if (get_included_files()[0] == __FILE__) {
    $di1 = DateInterval::createFromDateString('1 hour 20 minutes');
    $di2 = DateInterval::createFromDateString('2 hours 20 minutes');
    $di3 = DateInterval::createFromDateString('3 hours 34 minutes');

    // Note that the add method can accept any number of DateInterval objects.
    $diSum = DateIntervalMath::add($di1, $di2, $di3);
    echo "Sum: {$diSum->format('%h:%I:%S')}\n";

    $di4 = DateInterval::createFromDateString('4 hours 9 minutes');
    $di5 = DateInterval::createFromDateString('2 hours 21 minutes');

    $diDiff = DateIntervalMath::subtract($di4, $di5);
    echo "Diff: {$diDiff->format('%h:%I:%S')}\n";

    $di6 = DateInterval::createFromDateString('4 hours 36 minutes');
    $diProd = DateIntervalMath::multiply($di6, 5);
    echo "Product: {$diProd->format('%h:%I:%S')}\n";

    $di7 = DateInterval::createFromDateString('1 day');
    $diQuot = DateIntervalMath::divide($di7, 16);
    echo "Quotient: {$diQuot->format('%h:%I:%S')}\n";
}