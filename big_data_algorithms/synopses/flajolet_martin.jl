module FlajoletMartin

export hash_a, hash_b, hash_c, flajolet_martin, least_significant_bit, least_significant_zero

hash_a(x) = mod((2 * x + 1), 32)

hash_b(x) = mod((3 * x + 7), 32)

hash_c(x) = mod(4 * x, 32)

hash_e(x) = mod(3x + 5, 32)

Φ = 0.77351

function set_bit(x, index, bit)
    return (bit << index) | x
end

function trimmed_bitstring(x)
    bits = bitstring(x)
    return bits[leading_zeros(x)+1:end]
end

function least_significant_bit(x)
    # bits = trimmed_bitstring(x)
    # return length(bits) - trailing_zeros(x) - 1
    return trailing_zeros(x)
end

function least_significant_zero(x)
    bits = bitstring(x)
    L = length(bits)
    for i in L:-1:1
        if bits[i] == '0'
            return L - i
        end
    end
end

function flajolet_martin(stream, hash)
    bitmask = 0
    for x in stream;                      print(rpad("x: $x", 12))
        h = hash(x);                      print(rpad("h(x): $h", 12))
        t = least_significant_bit(h);     print(rpad("ρ(h(x)): $t", 12))
        bitmask = set_bit(bitmask, t, 1); println(rpad("bitmask: $(bitstring(bitmask))", 12))
    end
    r = least_significant_zero(bitmask)
    return (r, 2^r / Φ, bitmask)
end

end