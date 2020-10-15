include("../../big_data_algorithms/synopses/flajolet_martin.jl")
fa = FlajoletMartin

using Test

@testset "least signficant bit" begin
    @test fa.least_significant_bit(0) == 64
    @test fa.least_significant_bit(1) == 0
    @test fa.least_significant_bit(2) == 1
    @test fa.least_significant_bit(3) == 0
    @test fa.least_significant_bit(4) == 2
end