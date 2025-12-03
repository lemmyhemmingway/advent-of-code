defmodule Aoc2025.MixProject do
  use Mix.Project

  def project do
    [
      app: :aoc2025,
      version: "0.1.0",
      elixir: "~> 1.14",
      escript: [main_module: Aoc2025.CLI]
    ]
  end

  def application do
    [
      extra_applications: [:logger]
    ]
  end

  defp deps do
    []
  end
end
