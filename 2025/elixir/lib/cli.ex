defmodule Aoc2025.CLI do
  def main(args) do
    case args do
      [day] ->
        day_num = String.pad_leading(day, 2, "0")
        input_path = "../../inputs/day#{day_num}.txt"

        case File.read(input_path) do
          {:ok, input} ->
            module = Module.concat(Aoc2025, "Day#{day_num}")

            if Code.ensure_loaded?(module) do
              IO.puts("Part 1: #{module.part1(input)}")
              IO.puts("Part 2: #{module.part2(input)}")
            else
              IO.puts("Day #{day_num} not implemented")
              System.halt(1)
            end

          {:error, _} ->
            IO.puts("Input file #{input_path} not found")
            System.halt(1)
        end

      _ ->
        IO.puts("Usage: aoc <day>")
        System.halt(1)
    end
  end
end
