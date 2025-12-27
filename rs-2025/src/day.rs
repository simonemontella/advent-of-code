pub trait Day {
    fn name(&self) -> &'static str;
    fn number(&self) -> u8;

    fn part1(&self, input: &str) -> String;
    fn part2(&self, input: &str) -> String;
}