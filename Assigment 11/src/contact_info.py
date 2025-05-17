class ContactInfo:
    def __init__(self, email: str, phone: str, address: str):
        self._email = email
        self._phone = phone
        self._address = address
    
    @property
    def email(self) -> str:
        return self._email
    
    @email.setter
    def email(self, value: str):
        self._email = value
    
    @property
    def phone(self) -> str:
        return self._phone
    
    @phone.setter
    def phone(self, value: str):
        self._phone = value
    
    @property
    def address(self) -> str:
        return self._address
    
    @address.setter
    def address(self, value: str):
        self._address = value
    
    def validate(self) -> bool:
        """Validate contact information"""
        # Simple validation logic
        is_valid_email = '@' in self._email and '.' in self._email
        is_valid_phone = len(self._phone) >= 10 and self._phone.isdigit()
        is_valid_address = len(self._address) > 0
        
        return is_valid_email and is_valid_phone and is_valid_address
    
    def update(self, new_info) -> bool:
        """Update contact information with new values"""
        if isinstance(new_info, ContactInfo):
            self._email = new_info.email
            self._phone = new_info.phone
            self._address = new_info.address
            return True
        return False
