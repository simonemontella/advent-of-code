use crate::day::Day;
use std::fs;

pub struct Day02;

impl Day for Day02 {
    fn name(&self) -> &'static str {
        "Gift Shop"
    }

    fn number(&self) -> u8 {
        2
    }

    fn part1(&self, input: &str) -> String {
        let mut sum: i64 = 0;
        for entry in input.split(",").collect::<Vec<&str>>() {
            let range = Range::parse(entry);

            sum += range
                .get_even_items()
                .iter()
                .filter(|item| item[..item.len() / 2] == item[item.len() / 2..])
                .map(|item| item.parse::<i64>().unwrap())
                .sum::<i64>()
        }

        sum.to_string()
    }

    fn part2(&self, input: &str) -> String {
        let mut sum: i64 = 0;

        for entry in input.split(",").collect::<Vec<&str>>() {
            let range = Range::parse(entry);

            let invalids = range
                .items
                .iter()
                .filter(|item| has_sequences(&item.to_string(), item.to_string()))
                .collect::<Vec<&String>>();

            write(&format!(
                "Range: {}-{}, Invalid ids: {:?}\n",
                range.min, range.max, invalids
            ));

            sum += invalids
                .iter()
                .map(|item| item.parse::<i64>().unwrap())
                .sum::<i64>();
        }

        sum.to_string()
    }

    fn test(&self, test_input: &str) {
        let mut sum: i64 = 0;
        for entry in test_input.split(",").collect::<Vec<&str>>() {
            let range = Range::parse(entry);

            let invalids = range
                .items
                .iter()
                .filter(|item| has_sequences(&item.to_string(), item.to_string()))
                .collect::<Vec<&String>>();

            sum += invalids
                .iter()
                .map(|item| item.parse::<i64>().unwrap())
                .sum::<i64>();

            println!(
                "Range: {}-{}, Invalid ids: {:?}\nSUM: {}",
                range.min, range.max, invalids, sum
            );
        }
    }
}

fn has_sequences(start_item: &String, current_item: String) -> bool {
    if start_item.len() == 1 || current_item.len() == 0 {
        return false;
    }

    let mid = current_item.len().div_ceil(2);
    let left = &current_item[..mid];
    let pattern_len = left.len();

    if start_item.len() % pattern_len == 0
        && start_item
            .chars()
            .collect::<Vec<char>>()
            .chunks(pattern_len)
            .all(|w| {
                let segment: String = w.iter().collect();
                segment == left
            })
    {
        return true;
    } else if left.len() == 1 {
        return false;
    } else {
        return has_sequences(start_item, left.to_string());
    }
}

fn write(string: &str) {
    use std::io::Write;
    let mut file = fs::OpenOptions::new()
        .write(true)
        .append(true)
        .open("outputs/test_D2P2.txt")
        .unwrap();

    writeln!(file, "{}", string).unwrap();
}

struct Range {
    min: String,
    max: String,
    items: Vec<String>,
}

impl Range {
    fn parse(entry: &str) -> Self {
        let range_bounds: Vec<&str> = entry.split('-').collect();
        let min = range_bounds[0].trim().to_string().parse::<usize>().unwrap();
        let max = range_bounds[1].trim().to_string().parse::<usize>().unwrap();

        let mut items = Vec::<String>::new();

        for i in min..max + 1 {
            items.push(i.to_string());
        }

        Range {
            min: min.to_string(),
            max: max.to_string(),
            items,
        }
    }

    fn get_even_items(&self) -> Vec<String> {
        self.items
            .iter()
            .filter(|item| item.to_string().len() % 2 == 0)
            .cloned()
            .collect()
    }
}
