mod day;
mod days;

use day::Day;
use std::env;
use std::fs;

fn run_day(day: &dyn Day, test: bool) {
    let input_path: String = format!("inputs/day{:02}.txt", day.number());

    let input: String = fs::read_to_string(&input_path).unwrap_or_else(|e| {
        panic!("Impossibile recuperare l'input {}: {}", input_path, e);
    });

    println!("=== {}: {} ===", day.number(), day.name());
    if test {
        let test_path: String = format!("inputs/tests/day{:02}.txt", day.number());
        let test_input: String = fs::read_to_string(&test_path).unwrap_or_else(|e| {
            panic!(
                "Impossibile recuperare l'input di test {}: {}",
                test_path, e
            );
        });

        println!(
            "++ Test (P1): {} | (P2): {} ++",
            day.part1(&test_input),
            day.part2(&test_input)
        );

        day.test(&test_input);
    }

    println!("Part 1: {}", day.part1(&input));
    println!("Part 2: {}", day.part2(&input));
    println!();
}

fn main() {
    let days: Vec<&'static dyn Day> = vec![&days::Day01, &days::Day02, &days::Day03];

    println!("Advent of Code 2025");
    let args: Vec<String> = env::args().collect();

    let day: u8 = if args.len() > 1 {
        args[1]
            .parse()
            .expect("Inserisci un numero valido per il giorno")
    } else {
        0
    };

    let run_test: bool = if args.len() > 2 && args[2] == "--test" {
        true
    } else {
        false
    };

    if day == 0 {
        for d in &days {
            run_day(*d, run_test);
        }
    } else {
        run_day(days[day as usize - 1], run_test);
    }
}
