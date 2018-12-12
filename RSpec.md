# RSpec

- Tests are the first client of your code.
- Your tests provide evidence that the application works, but they certainly don’t provide proof

## Examples

```ruby
class Coffee
  def ingredients
    @ingredients ||= []
  end

  def add(ingredient)
    ingredients << ingredient
  end

  def price
    1.00
  end
end

RSpec.describe 'A cup of coffee' do
  let(:coffee) { Coffee.new }

  it 'costs $1' do
    expect(coffee.price).to eq(1.00)
  end

  context 'with milk' do
    before { coffee.add :milk }

    it 'costs $1.25' do
      expect(coffee.price).to eq(1.25)
    end
  end
end
```