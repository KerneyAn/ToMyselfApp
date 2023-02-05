@main
public struct ToMyself {
    public private(set) var text = "Hello, World!"

    public static func main() {
        print(ToMyself().text)
    }
}
