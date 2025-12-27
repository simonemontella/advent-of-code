use crate::day::Day;

pub struct Day01;

impl Day for Day01 {
    fn name(&self) -> &'static str {
        "Secret Entrance"
    }

    fn number(&self) -> u8 {
        1
    }

    fn part1(&self, input: &str) -> String {
        let mut current_point: i32 = 50;
        let mut password = 0; //zeros count

        for line in input.lines() {
            let multiplier: i32 = if &line[..1] == "R" { 1 } else { -1 };

            current_point += multiplier * (line[1..].parse::<i32>().unwrap());
            password += if current_point.abs() % 100 == 0 { 1 } else { 0 }
        }

        password.to_string()
    }

    fn part2(&self, input: &str) -> String {
        "Not implemented".to_string()
    }
}
