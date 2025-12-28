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
            let direction: i32 = if &line[..1] == "R" { 1 } else { -1 };
            let step: i32 = line[1..].parse::<i32>().unwrap();

            current_point += direction * step;
            password += if current_point.abs() % 100 == 0 { 1 } else { 0 }
        }

        password.to_string()
    }

    fn part2(&self, input: &str) -> String {
        let mut current_point: i32 = 50;
        let mut password = 0; //zeros count + zero crossings

        for line in input.lines() {
            let direction: i32 = if &line[..1] == "R" { 1 } else { -1 };
            let step: i32 = line[1..].parse::<i32>().unwrap();

            let next_point = (current_point + (direction * step)).rem_euclid(100);

            let dist_zero = if direction > 0 {
                (100 - current_point) % 100
            } else {
                current_point
            };

            let crosses_zero = if step < dist_zero {
                0
            } else if dist_zero == 0 {
                step / 100
            } else {
                1 + (step - dist_zero) / 100
            };

            password += crosses_zero;

            current_point = next_point;
        }

        password.to_string()
    }

    fn test(&self, test_input: &str) {}
}
