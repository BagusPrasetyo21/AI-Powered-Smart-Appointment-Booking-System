from abc import ABC, abstractmethod

class Button(ABC):
    """Abstract Product: Button"""
    @abstractmethod
    def render(self) -> str:
        pass
    
    @abstractmethod
    def on_click(self) -> str:
        pass

class TextField(ABC):
    """Abstract Product: TextField"""
    @abstractmethod
    def render(self) -> str:
        pass
    
    @abstractmethod
    def on_input(self, value: str) -> str:
        pass

class UIFactory(ABC):
    """Abstract Factory Interface"""
    @abstractmethod
    def create_button(self, label: str) -> Button:
        pass
    
    @abstractmethod
    def create_text_field(self, placeholder: str) -> TextField:
        pass

# Concrete Products for Web UI
class WebButton(Button):
    def __init__(self, label: str):
        self.label = label
    
    def render(self) -> str:
        return f'<button class="web-button">{self.label}</button>'
    
    def on_click(self) -> str:
        return f'Web button "{self.label}" clicked'

class WebTextField(TextField):
    def __init__(self, placeholder: str):
        self.placeholder = placeholder
    
    def render(self) -> str:
        return f'<input type="text" placeholder="{self.placeholder}" class="web-text-field">'
    
    def on_input(self, value: str) -> str:
        return f'Web text field with placeholder "{self.placeholder}" received input: {value}'

# Concrete Products for Mobile UI
class MobileButton(Button):
    def __init__(self, label: str):
        self.label = label
    
    def render(self) -> str:
        return f'[MobileButton label="{self.label}"]'
    
    def on_click(self) -> str:
        return f'Mobile button "{self.label}" tapped'

class MobileTextField(TextField):
    def __init__(self, placeholder: str):
        self.placeholder = placeholder
    
    def render(self) -> str:
        return f'[MobileTextField hint="{self.placeholder}"]'
    
    def on_input(self, value: str) -> str:
        return f'Mobile text field with hint "{self.placeholder}" received input: {value}'

# Concrete Factories
class WebUIFactory(UIFactory):
    """Concrete Factory for Web UI components"""
    def create_button(self, label: str) -> Button:
        return WebButton(label)
    
    def create_text_field(self, placeholder: str) -> TextField:
        return WebTextField(placeholder)

class MobileUIFactory(UIFactory):
    """Concrete Factory for Mobile UI components"""
    def create_button(self, label: str) -> Button:
        return MobileButton(label)
    
    def create_text_field(self, placeholder: str) -> TextField:
        return MobileTextField(placeholder)

# Client code
class AppointmentBookingUI:
    """
    Client class that uses the Abstract Factory
    
    This demonstrates how the UI can be created for different platforms
    without changing the client code.
    """
    def __init__(self, factory: UIFactory):
        self.factory = factory
        self.book_button = factory.create_button("Book Appointment")
        self.cancel_button = factory.create_button("Cancel")
        self.date_field = factory.create_text_field("Select Date")
        self.time_field = factory.create_text_field("Select Time")
    
    def render_booking_form(self) -> str:
        """Render the booking form using the factory's components"""
        return f"""
        Appointment Booking Form:
        {self.date_field.render()}
        {self.time_field.render()}
        {self.book_button.render()}
        {self.cancel_button.render()}
        """
    
    def handle_booking(self, date: str, time: str) -> str:
        """Handle the booking action"""
        date_response = self.date_field.on_input(date)
        time_response = self.time_field.on_input(time)
        button_response = self.book_button.on_click()
        
        return f"""
        Booking Processed:
        {date_response}
        {time_response}
        {button_response}
        """
