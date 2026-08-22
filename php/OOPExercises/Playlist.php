<?php
/*****
 * EXERCISE
 * Create a Playlist class that accepts and stores several Song class objects.
 * The Playlist should be able to add Songs, remove Songs by title, and shuffle Songs.
 */

namespace Aksman\Exercises\php\OOPExercises;
use ArrayIterator;
use Countable;
use DateInterval;
use DateTimeImmutable;
use IteratorAggregate;
use Traversable;
use Random\Randomizer;

class Song
{
    public string $title;
    public string $artist;
    public DateInterval $duration;

    public function __construct(string $title, string $artist, string $duration)
    {
        $this->title = $title;
        $this->artist = $artist;
        // Accept a string like "3:24" as defining the duraction of the song.
        // Internally convert that string notation into a DateInterval object.
        [$minutes, $seconds] = explode(':', $duration);
        $this->duration = DateInterval::createFromDateString("{$minutes} minutes + {$seconds} seconds");
    }

    // __toString() is a magic function we can use define how this class represents itself when 
    // converted into a string.
    public function __toString()
    {
        return "\"{$this->title}\" by {$this->artist}";
    }

    // Output the duration as a human readable string.
    public function durationStr()
    {
        return $this->duration->format('%i:%S');
    }

}

// Two special PHP interfaces are used here.
// IteratorAggregate allows us to define what happens if we try to loop over the Playlist,
// for example in a foreach() loop.
// Countable allows us to define what happens when we use the count() function on this class.
// In order to fully use this functionality, we need to both specify that our class
// "implements" the interfaces, and define the requisite functions.
class Playlist implements IteratorAggregate, Countable
{
    // Internal array to store the Songs in.
    private array $list = [];

    // This constructor uses a "splat" operator, meaning $songs will be an array containing 
    // any number of Songs.
    public function __construct(Song ...$songs)
    {
        $this->list = array_values($songs);
    }

    // The add function also uses a "splat" operator, making this also a variadic function
    // where we can have any number of Songs.
    public function add(Song ...$songs): void
    {
        $this->list = array_merge($this->list, $songs);
    }

    // Remove a song with the specified title from the Playlist.
    public function remove(string $songTitle): void
    {
        // We use array_filter to return all the Songs which don't match the title.
        // We have to use the "use" keyword so that out filtering function has access to
        // our $songTitle. Otherwise, it would be outside the scope of the function.
        $this->list = array_values(array_filter($this->list, function(Song $song) use ($songTitle) {
            return $song->title !== $songTitle;
        }));
    }

    // This implements the IteratorAggregate interface. It allows us to loop through the Songs
    // in the Playlist using regulat PHP structures like foreach().
    public function getIterator(): Traversable
    {
        return new ArrayIterator($this->list);
    }

    // This implements the Countable interface. It allows us to use PHP's count() function to 
    // find how many Songs are in the Playlist.
    public function count(): int
    {
        return count($this->list);
    }

    // Shuffle the Songs in our Playlist. This uses Random\Randomizer::shuffleArray(),
    // introduced in PHP 8.2, which is now the prefered method of randomly shuffling an array.
    public function shuffle(): void
    {
        $r = new Randomizer();
        $this->list = $r->shuffleArray($this->list);
    }

    // A method to find the total runtime of the Songs in the Playlist
    public function runtime(): string
    {
        // Unfortunately we cannot simply add DateIntervals together.
        // We need to set up a reference point in time, then add the 
        // DateIntervals to it, then find the DateInterval between the two
        // DateTimeImmutable objects.
        $baseTime = new DateTimeImmutable('2000-01-01 00:00:00');
        $accumulatedTime = $baseTime;

        foreach($this->list as $song) {
            $accumulatedTime = $accumulatedTime->add($song->duration);
        }

        $totalDuration =  $baseTime->diff($accumulatedTime);
        // If the duration is an hour or over, include hours in the string representation
        // of the total runtime.
        if($this->_durationOverOneHour($totalDuration)) {
            return $totalDuration->format('%h:%I:%s');
        } else {
            return $totalDuration->format('%i:%S');
        }
    }

    // A helper function to determine if a DateInterval object is a hour or longer.
    private function _durationOverOneHour(DateInterval $dateInterval): bool
    {
        $baseTime = new DateTimeImmutable('2000-01-01 00:00:00');
        $reference = $baseTime->add($dateInterval);
        return $reference->getTimestamp() - $baseTime->getTimestamp() >= 3600;
    }
}

// Run this block only if the script is being run directly, i.e. not included.
if (get_included_files()[0] == __FILE__) {
    $mixtape = new Playlist(
        new Song("I'm So Sick", 'Flyleaf', '2:55'),
        new Song('Dear Agony', 'Breaking Benjamin ft. Lacey Sturm', '4:19'),
        new Song('And the Rest is Mystery', 'Project Aegis', '9:07'),
        new Song('crushcrushcrush', 'Paramore', '3:10'),
        new Song('Over You', 'Daughtry', '3:45')
    );

    $c = count($mixtape);
    echo "{$c} songs total.\n\n";

    foreach($mixtape as $song) {
        echo "{$song} ({$song->durationStr()})\n";
    }

    echo "\n";

    $mixtape->shuffle();
    $mixtape->remove('crushcrushcrush');
    $mixtape->add(new Song('Puppet', 'Thousand Foot Krutch', '3:29'), new Song('Easter', 'Theocracy', '9:53'));
    echo "SHUFFLED ORDER\n";
    foreach($mixtape as $song) {
        echo "{$song} ({$song->durationStr()})\n";
    }
    echo "Runtime: {$mixtape->runtime()}";
}