use crate::day::Day;

pub struct Day03;

impl Day for Day03 {
    fn name(&self) -> &'static str {
        "Lobby"
    }

    fn number(&self) -> u8 {
        3
    }

    fn part1(&self, input: &str) -> String {
        let mut output_joltage: i64 = 0;

        for line in input.lines() {
            output_joltage += get_max_joltage(line.to_string(), 2);
        }

        output_joltage.to_string()
    }

    fn part2(&self, input: &str) -> String {
        let mut output_joltage: i64 = 0;

        for line in input.lines() {
            output_joltage += get_max_joltage(line.to_string(), 12);
        }

        output_joltage.to_string()
    }

    fn test(&self, test_input: &str) {
        for line in test_input.lines() {
            println!(
                "LINE: {}, MAX: {:?}",
                line,
                get_max_joltage(line.to_string(), 12)
            );
        }
    }
}

fn get_max_joltage(string: String, batteries: usize) -> i64 {
    let mut joltage = String::from("");
    let mut last_index: usize = 0;
    let lenght = string.len();

    for i in 0..batteries {
        let range = string[last_index..lenght - batteries + i + 1].to_string();
        let (index, value) = get_max(range.clone());

        last_index += index + 1;
        joltage.push(value);
    }

    joltage.parse::<i64>().unwrap()
}

fn get_max(string: String) -> (usize, char) {
    let chars = string.chars().collect::<Vec<char>>();
    let max = chars.iter().max().unwrap();
    let index = chars.iter().position(|&r| r == *max).unwrap();
    (index, *max)
}
