class MetricCard:

    def __init__(self, value: str, label: str, is_highlight: bool = False):
        self.value = value
        self.label = label
        self.is_highlight = is_highlight


class ServiceOffer:

    def __init__(self, title: str, description: str, icon: str, is_featured: bool = False):
        self.title = title
        self.description = description
        self.icon = icon
        self.is_featured = is_featured


class LeaderProfile:

    def __init__(
        self,
        name: str,
        role: str,
        bio: str,
        initials: str,
        phone: str = '',
        is_executive: bool = False,
    ):
        self.name = name
        self.role = role
        self.bio = bio
        self.initials = initials
        self.phone = phone
        self.is_executive = is_executive
