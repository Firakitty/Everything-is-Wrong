import random
from enum import Enum, Flag, auto
from typing import Union
from scripts.game_structure.game_essentials import game

class SkillPath(Enum):
    TEACHER = (
        "please help me quickly",
        "it is cold",
        "administrator",
        "the best teacher"
    )
    HUNTER =  (
        "the great ball hunter",
        "happy hunting",
        "hunter",
        "the famous hunter"
    )
    FIGHTER = (
        "good",
        "the good soldier",
        "bad fighter",
        "a very strong fighter."
    )
    RUNNER = (
        "it never settles down.",
        "run fast",
        "the great room",
        "quick as the wind"
    )
    CLIMBER = (
        "always upward",
        "good luck",
        "the greatest climber",
        "a good poet"
    )
    SWIMMER = (
        "spray in water",
        "take a good shower",
        "good bath",
        "swim like a fish"
    )
    SPEAKER = (
        "the right word",
        "good word",
        "speech",
        "speak"
    )
    MEDIATOR = (
        "hope you get well soon",
        "good broker",
        "great middle"
        "skill moderator"
    )
    CLEVER = (
        "soon",
        "later",
        "very intelligent",
        "wonderful wisdom"
    )
    INSIGHTFUL = (
        "pay attention",
        "good understanding",
        "true meaning",
        "the faithful steward"
    )
    SENSE = (
        "it's a beautiful sight",
        "natural instinct",
        "blind eye",
        "negative thought"
    )
    KIT = (
        "strong Life",
        "good cat",
        "great grandmother",
        "sweet kiss"
    )
    STORY = (
        "love story",
        "good talker",
        "the great singer",
        "history teacher"
    )
    LORE = (
        "genealogy of love",
        "students are studying",
        "guardian of culture",
        "famous masters"
    )
    CAMP = (
        "the nest builder",
        "standing wave",
        "light",
        "park rangers"
    )
    HEALER = (
        "the wonders of plants",
        "good deal",
        "doctor",
        "a beautiful healer"
    )
    STAR = (
        "funny about StarClan",
        "star web link",
        "deep StarClan bonds",
        "stern without flies"
    )
    DARK = (
        "witch of the Dark Forest",
        "exploring the Dark Forest",
        "link deep dark forest",
        "unbreakable link to the Dark One."
    )
    OMEN = (
        "I like rice",
        "search",
        "spring feeling",
        "signature"
    )
    DREAM = (
        "sleep",
        "strange dream",
        "dream manager",
        "the dreamer"
    )
    CLAIRVOYANT = (
        "foreign knowledge",
        "love",
        "the little nurse",
        "it is not surprising"
    )
    PROPHET = (
        "crazy prophecy",
        "seeker of the prophet",
        "The interpreter of prophecy",
        "ATM"
    )
    GHOST = (
        "sick love"
        "conscience",
        "vision of ghosts",
        "ghostbuster"
    )
   
    @staticmethod
    def get_random(exclude:list=()):
        """Get a random path, with more uncommon paths being less common"""
       
        uncommon_paths = [i for i in [SkillPath.GHOST, SkillPath.PROPHET,
                          SkillPath.CLAIRVOYANT, SkillPath.DREAM,
                          SkillPath.OMEN, SkillPath.STAR, SkillPath.HEALER,
                          SkillPath.DARK]
                          if i not in exclude]
       
       
        if not int(random.random() * 15):
            return random.choice(uncommon_paths)
        else:
            common_paths = [i for i in list(SkillPath) if
                           i not in exclude and i not in uncommon_paths]
            return random.choice(common_paths)


   
class HiddenSkillEnum(Enum):
    ROGUE = "rogue's knowledge"
    LONER = "loner's knowledge"
    KITTYPET = "kittypet's knowledge"
   
class SkillTypeFlag(Flag):
    SUPERNATURAL = auto()
    STRONG = auto()
    AGILE = auto()
    SMART = auto()
    OBSERVANT = auto()
    SOCIAL = auto()
   
class Skill():
    '''Skills handling functions mostly'''
   
    tier_ranges = ((0, 9), (10, 19), (20, 29))
    point_range = (0, 29)
   
    short_strings = {
        SkillPath.TEACHER: "training",
        SkillPath.HUNTER: "chase",
        SkillPath.FIGHTER: "war",
        SkillPath.RUNNER: "run me",
        SkillPath.CLIMBER: "get out",
        SkillPath.SWIMMER: "bath in water",
        SkillPath.SPEAKER: "number",
        SkillPath.MEDIATOR: "center stage",
        SkillPath.CLEVER: "later",
        SkillPath.INSIGHTFUL: "interview",
        SkillPath.SENSE: "apply",
        SkillPath.KIT: "circle",
        SkillPath.STORY: "confirm it",
        SkillPath.LORE: "watchman",
        SkillPath.CAMP: "camp management",
        SkillPath.HEALER: "invoice",
        SkillPath.STAR: "alone",
        SkillPath.OMEN: "tracking",
        SkillPath.DREAM: "dream",
        SkillPath.CLAIRVOYANT: "on standby",
        SkillPath.PROPHET: "inform them",
        SkillPath.GHOST: "spirit",
        SkillPath.DARK: "black forest",
    }

    
    
    def __init__(self, path:SkillPath, points:int=0, interest_only:bool=False):
        
        self.path = path
        self.interest_only = interest_only
        if points > self.point_range[1]:
            self._p = self.point_range[1]
        elif points < self.point_range[0]:
            self._p = self.point_range[0]
        else:
            self._p = points
    
    def __repr__(self) -> str:
        return f"<Skill: {self.path}, {self.points}, {self.tier}, {self.interest_only}>" 
    
    def get_short_skill(self):
        return Skill.short_strings.get(self.path, "???")
    
    @staticmethod
    def generate_from_save_string(save_string:str):
        '''Generates the skill from the save string in the cat data'''
        if not save_string:
            return None
        
        split_values = save_string.split(",")
        if split_values[2].lower() == "true":
            interest = True
        else:
            interest = False
        
        return Skill(SkillPath[split_values[0]], int(split_values[1]), interest)
    
    @staticmethod
    def get_random_skill(points:int = None, point_tier:int = None, exclude=(), interest_only=False):
        """Generates a random skill. If wanted, you can specify a tier for the points
        value to be randomized within. """
        
        if isinstance(points, int):
            points = points
        elif isinstance(point_tier, int) and 1 <= point_tier <= 3:
            points = random.randint(Skill.tier_ranges[point_tier-1][0], Skill.tier_ranges[point_tier-1][1])
        else:
            points = random.randint(Skill.point_range[0], Skill.point_range[1])
        
        
        if isinstance(exclude, SkillPath):
            exclude = [exclude]

        return Skill(SkillPath.get_random(exclude), points, interest_only)
    
    @property
    def points(self):
        return self._p
    
    @points.setter
    def points(self, val):
        if val > self.point_range[1]:
            self._p = self.point_range[1]
        elif val < self.point_range[0]:
            self._p = self.point_range[0]
        else:
            self._p = val
        
    @property
    def skill(self):
        '''Skill property'''
        return self.path.value[self.tier]
        
    @skill.setter
    def skill(self):
        '''Can't set the skill directly with this setter'''
        print("Can't set skill directly")
    
    @property
    def tier(self):
        '''Returns the tier level of the skill'''
        if self.interest_only:
            return 0 
        for _ran, i in zip(Skill.tier_ranges, range(1, 4)):
            if _ran[0] <= self.points <= _ran[1]:
                return i
                
        return 1
    
    @tier.setter
    def tier(self):
        print("Can't set tier directly")
    
    def set_points_to_tier(self, tier:int):
        """This is seperate from the tier setter, since it will booonly allow you
        to set points to tier 1, 2, or 3, and never 0. Tier 0 is retricted to interest_only
        skills"""
        
        # Make sure it in the right range. If not, return. 
        if not (1 <= tier <= 3):
            return
        
        # Adjust to 0-indexed ranges list
        self.points = Skill.tier_ranges[tier - 1][0]
        
    def get_save_string(self):
        '''Gets the string that is saved in the cat data'''
        return f"{self.path.name},{self.points},{self.interest_only}"

class CatSkills:
    """
    Holds the cats skills, and handled changes in the skills. 
    """

    #Mentor Inflence groups.
    # pylint: disable=unsupported-binary-operation
    influence_flags = {
        SkillPath.TEACHER: SkillTypeFlag.STRONG | SkillTypeFlag.AGILE | SkillTypeFlag.SMART | SkillTypeFlag.OBSERVANT | SkillTypeFlag.SOCIAL,
        SkillPath.HUNTER: SkillTypeFlag.STRONG | SkillTypeFlag.AGILE | SkillTypeFlag.OBSERVANT,
        SkillPath.FIGHTER: SkillTypeFlag.STRONG | SkillTypeFlag.AGILE,
        SkillPath.RUNNER: SkillTypeFlag.AGILE,
        SkillPath.CLIMBER: SkillTypeFlag.STRONG | SkillTypeFlag.AGILE,
        SkillPath.SWIMMER: SkillTypeFlag.STRONG | SkillTypeFlag.AGILE,
        SkillPath.SPEAKER: SkillTypeFlag.SOCIAL | SkillTypeFlag.SMART,
        SkillPath.MEDIATOR: SkillTypeFlag.SMART | SkillTypeFlag.SOCIAL,
        SkillPath.CLEVER: SkillTypeFlag.SMART,
        SkillPath.INSIGHTFUL: SkillTypeFlag.SMART | SkillTypeFlag.OBSERVANT,
        SkillPath.SENSE: SkillTypeFlag.OBSERVANT,
        SkillPath.KIT: SkillTypeFlag.SOCIAL,
        SkillPath.STORY: SkillTypeFlag.SMART | SkillTypeFlag.SOCIAL,
        SkillPath.LORE: SkillTypeFlag.SMART | SkillTypeFlag.SOCIAL,
        SkillPath.CAMP: SkillTypeFlag.OBSERVANT | SkillTypeFlag.SOCIAL,
        SkillPath.HEALER: SkillTypeFlag.SMART | SkillTypeFlag.OBSERVANT | SkillTypeFlag.SOCIAL,
        SkillPath.STAR: SkillTypeFlag.SUPERNATURAL,
        SkillPath.OMEN: SkillTypeFlag.SUPERNATURAL | SkillTypeFlag.OBSERVANT,
        SkillPath.DREAM: SkillTypeFlag.SUPERNATURAL,
        SkillPath.CLAIRVOYANT: SkillTypeFlag.SUPERNATURAL | SkillTypeFlag.OBSERVANT,
        SkillPath.PROPHET: SkillTypeFlag.SUPERNATURAL,
        SkillPath.GHOST: SkillTypeFlag.SUPERNATURAL,
        SkillPath.DARK: SkillTypeFlag.SUPERNATURAL,
    }
    # pylint: enable=unsupported-binary-operation
    
    def __init__(self,
                 skill_dict=None,
                 primary_path:SkillPath = None,
                 primary_points:int = 0,
                 secondary_path: SkillPath = None,
                 secondary_points:int = 0,
                 hidden_skill:HiddenSkillEnum = None,
                 interest_only=False):
        

        if skill_dict:
            self.primary = Skill.generate_from_save_string(skill_dict["primary"])
            self.secondary = Skill.generate_from_save_string(skill_dict["secondary"])
            self.hidden = HiddenSkillEnum[skill_dict["hidden"]] if skill_dict["hidden"] else None
        else:
            if primary_path:
                self.primary = Skill(primary_path, primary_points, interest_only)
            else:
                self.primary = None
            if secondary_path:
                self.secondary = Skill(secondary_path, secondary_points, interest_only)
            else:
                self.secondary = None
            
            self.hidden = hidden_skill
    
    def __repr__(self) -> str:
        return f"<CatSkills: Primary: |{self.primary}|, Secondary: |{self.secondary}|, Hidden: |{self.hidden}|>"
    
    @staticmethod
    def generate_new_catskills(status, moons, hidden_skill:HiddenSkillEnum=None):
        '''Generates a new skill'''
        new_skill = CatSkills()
        
        new_skill.hidden = hidden_skill       

        #TODO: Make this nicer
        if status == "newborn" or moons <= 0:
            pass
        elif status == 'kitten' or moons < 6:
            new_skill.primary = Skill.get_random_skill(points=0, interest_only=True)
        elif status == 'apprentice':
            new_skill.primary = Skill.get_random_skill(point_tier=1, interest_only=True)
            if random.randint(1, 3) == 1:
                new_skill.secondary = Skill.get_random_skill(point_tier=1, interest_only=True, exclude=new_skill.primary.path)
        elif moons < 50:
            new_skill.primary = Skill.get_random_skill(point_tier=random.randint(1, 2))
            if random.randint(1, 2) == 1:
                new_skill.secondary = Skill.get_random_skill(point_tier=random.randint(1, 2), exclude=new_skill.primary.path)
        elif moons < 100:
            new_skill.primary = Skill.get_random_skill(point_tier=random.randint(1, 3))
            if random.randint(1, 2) == 1:
                new_skill.secondary = Skill.get_random_skill(point_tier=random.randint(1, 2), exclude=new_skill.primary.path)
        elif moons < 150:
            new_skill.primary = Skill.get_random_skill(point_tier=random.randint(2, 3))
            if random.randint(1, 2) == 1:
                new_skill.secondary = Skill.get_random_skill(point_tier=random.randint(1, 2), exclude=new_skill.primary.path)
        else:
            new_skill.primary = Skill.get_random_skill(point_tier=1)
            if random.randint(1, 2) == 1:
                new_skill.secondary = Skill.get_random_skill(point_tier=1, exclude=new_skill.primary.path)
        
        return new_skill
            
    def get_skill_dict(self):
        return {
            "primary": self.primary.get_save_string() if self.primary else None,
            "secondary": self.secondary.get_save_string() if self.secondary else None, 
            "hidden": self.hidden.name if self.hidden else None
        }

    def skill_string(self, short=False):
        output = []
        
        if short:
            if self.primary:
                output.append(self.primary.get_short_skill())
            if self.secondary:
                output.append(self.secondary.get_short_skill())
        else:
            if self.primary:
                output.append(self.primary.skill)
            if self.secondary:
                output.append(self.secondary.skill)

        if not output:
            return "???"

        return " & ".join(output)

    def mentor_influence(self, mentor):
        """
        this function handles mentor influence on the cat's skill
        :param the_cat: the cat object
        :param mentor: the mentor's cat object
        """

        if not mentor:
            return
        
        # Determine if any skills can be effected
        mentor_tags = CatSkills.influence_flags[mentor.skills.primary.path] if mentor.skills.primary else None

        can_primary = bool(
            CatSkills.influence_flags[self.primary.path] & mentor_tags) if self.primary and mentor_tags else False
        can_secondary = bool(
            CatSkills.influence_flags[self.secondary.path] & mentor_tags) if self.secondary and mentor_tags else False
            
        # If nothing can be effected, just return as well.         
        if not (can_primary or can_secondary):
            return

        amount_effect = random.randint(1, 4)
        
        if can_primary and can_secondary:
            if random.randint(1, 2) == 1:
                self.primary.points += amount_effect
                path = self.primary.path
            else:
                self.secondary.points += amount_effect
                path = self.secondary.path
        elif can_primary:
            self.primary.points += amount_effect
            path = self.primary.path
        else:
            self.secondary.points += amount_effect
            path = self.secondary.path
    
        return (mentor.ID, path, amount_effect)

    def progress_skill(self, the_cat):
        """
        this function should be run every moon for every cat to progress their skills accordingly
        :param the_cat: the cat object for affected cat
        """
        
        if the_cat.status == 'newborn' or the_cat.moons <= 0:
            return
        
        # Give a primary is there isn't one already, and the cat is older than one moon. 
        if not self.primary:
            parents = [the_cat.fetch_cat(i) for i in [the_cat.parent1, the_cat.parent2] + the_cat.adoptive_parents if 
                    type(the_cat) == type(the_cat.fetch_cat(i))]
            parental_paths = [i.skills.primary.path for i in parents if i.skills.primary] + [i.skills.secondary.path for i in parents if i.skills.secondary]
                    
            # If there are parental paths, flip a coin to determine if they will get a parents path
            if parental_paths and random.randint(0, 1):
                self.primary = Skill(random.choice(parental_paths), points=0, interest_only=True if the_cat.status in ["apprentice", "kitten"] else False)
            else:
                self.primary = Skill.get_random_skill(points=0, interest_only=True if the_cat.status in ["apprentice", "kitten"] else False)
        
        
        if not (the_cat.outside or the_cat.exiled):
                        
            if the_cat.status == 'kitten':
                # Check to see if the cat gains a secondary
                if not self.secondary and not int(random.random() * 22):
                    # if there's no secondary skill, try to give one!
                    self.secondary = Skill.get_random_skill(points=0, interest_only=True, exclude=self.primary.path)
                
                # if the the_cat has skills, check if they get any points this moon
                if not int(random.random() * 4):
                    amount_effect = random.randint(1, 4)
                    if self.primary and self.secondary:
                        if random.randint(1, 2) == 1:
                            self.primary.points += amount_effect
                        else:
                            self.secondary.points += amount_effect
                    elif self.primary:
                        self.primary.points += amount_effect

            elif 'apprentice' in the_cat.status:
                # Check to see if the cat gains a secondary
                if not self.secondary and not int(random.random() * 22):
                    # if there's no secondary skill, try to give one!
                    self.secondary = Skill.get_random_skill(points=0, interest_only=True, exclude=self.primary.path)
                
                # Check if they get any points this moon
                if not int(random.random() * 4):
                    amount_effect = random.randint(2, 5)
                    if self.primary and self.secondary:
                        if random.randint(1, 2) == 1:
                            self.primary.points += amount_effect
                        else:
                            self.secondary.points += amount_effect
                    elif self.primary:
                        self.primary.points += amount_effect

            elif the_cat.moons > 120:
                # for old cats, we want to check if the skills start to degrade at all, age is the great equalizer
                
                self.primary.interest_only = False
                if self.secondary:
                    self.secondary.interest_only = False
                
                chance = max(1, 160 - the_cat.moons)
                if not int(random.random() * chance):  # chance increases as the_cat ages
                    self.primary.points -= 1
                    if self.secondary:
                        self.secondary.points -= 1
            else:
                #If they are still in "interest" stage, there is a change to swap primary and secondary
                # If they are still in "interest" but reached this part, they just graduated. 
                if self.primary.interest_only and self.secondary:
                    flip = random.choices([False, True], [self.primary.points + 1, 
                                                        self.secondary.points + 1])[0]
                    if flip:
                        _temp = self.primary
                        self.primary = self.secondary
                        self.secondary = _temp
                
                self.primary.interest_only = False
                if self.secondary:
                    self.secondary.interest_only = False
                    
                # If a cat doesn't can a secondary, have a small change for them to get one. 
                # but, only a first-tier skill. 
                if not self.secondary and not int(random.random() * 300):
                    self.secondary = Skill.get_random_skill(exclude=self.primary.path, point_tier=1)
                
                # There is a change for primary to condinue to improve throughout life 
                # That chance decreases as the cat gets older. 
                # This is to simulate them reaching their "peak"
                if not int(random.random() * int(the_cat.moons/4)):
                    self.primary.points += 1  
        else:
            # For outside cats, just check interest and flip it if needed. 
            # Going on age, rather than status here. 
            if the_cat.age not in ["kitten", "adolescent"]:
                self.primary.interest_only = False
                if self.secondary:
                    self.secondary.interest_only = False
    
    def meets_skill_requirement(self, path: Union[str, SkillPath, HiddenSkillEnum], min_tier:int=0) -> bool:
        """Checks both primary and seconday, to see if cat matches skill restaint"""
        
        if isinstance(path, str):
            # Try to conter to Skillpath or HiddenSkillEnum
            try:
                path = SkillPath[path]
            except KeyError:
                try:
                    path = HiddenSkillEnum[path]
                except KeyError:
                    print(f"{path} is not a real skill path")
                    return False
        
        if isinstance(path, HiddenSkillEnum):
            if path == self.hidden:
                return True
        elif isinstance(path, SkillPath):
            if self.primary:
                if path == self.primary.path and self.primary.tier >= min_tier:
                    return True
            
            if self.secondary:
                if path == self.secondary.path and self.secondary.tier >= min_tier:
                    return True
        
        return False
    
    def check_skill_requirement_list(self, skill_list:list) -> int:
        """Takes a whole list of skill requirments in the form 
            [ "SKILL_PATH,MIN_TIER" ... ] and determines how many skill
            requirments are meet. The list format is used in all patrol and event skill
            restrictions. Returns an integer value of how many skills requirments are meet.  
            """
        
        skills_meet = 0
        
        min_tier = 0
        for _skill in skill_list:
            spl = _skill.split(",")
            
            if len(spl) != 2:
                print("Incorrectly formatted skill restriction", _skill)
                continue
            
            try:
                min_tier = int(spl[1])
            except ValueError:
                print("Min Skill Tier cannot be converted to int", _skill)
                continue
            
            if self.meets_skill_requirement(spl[0], min_tier):
                skills_meet += 1
        
        return skills_meet
                     
    
    @staticmethod
    def get_skills_from_old(old_skill, status, moons):
        """Generates a CatSkill object"""
        
        new_skill = CatSkills()
        
        conversion = {
            "deep StarClan bonds": (SkillPath.STAR, 2), 
            "the wonders of plants": (SkillPath.HEALER, 1),
            "a beautiful healer": (SkillPath.HEALER, 2),
            "funny about StarClan": (SkillPath.HEALER, 3),
            "speech": (SkillPath.TEACHER, 1),
            "good talker": (SkillPath.TEACHER, 2),
            "history teacher": (SkillPath.TEACHER, 3),
            "hope you get well soon": (SkillPath.MEDIATOR, 1),
            "good broker": (SkillPath.MEDIATOR, 2),
            "skill moderator": (SkillPath.MEDIATOR, 3),
            "wonderful wisdom": (SkillPath.CLEVER, 1),
            "very intelligent": (SkillPath.CLEVER, 2),
            "later": (SkillPath.CLEVER, 3),
            "the famous hunter": (SkillPath.HUNTER, 1),
            "happy hunting": (SkillPath.HUNTER, 2),
            "fantastic hunter": (SkillPath.HUNTER, 3),
            "a very strong fighter.": (SkillPath.FIGHTER, 1),
            "the good soldier": (SkillPath.FIGHTER, 2),
            "bad fighter": (SkillPath.FIGHTER, 3),
            "speak": (SkillPath.SPEAKER, 1),
            "good word": (SkillPath.SPEAKER, 2),
            "excellent speaker": (SkillPath.SPEAKER, 3),
            "the great singer": (SkillPath.STORY, 1),
            "good talker": (SkillPath.STORY, 2),
            "fantastic storyteller": (SkillPath.STORY, 3),
            "pay attention": (SkillPath.INSIGHTFUL, 1),
            "good understanding": (SkillPath.INSIGHTFUL, 2),
            "true meaning": (SkillPath.INSIGHTFUL, 3),
            "sweet kiss": (SkillPath.KIT, 1),
            "good cat": (SkillPath.KIT, 2),
            "great grandmother": (SkillPath.KIT, 3),
            "the nest builder": (SkillPath.CAMP, 3),
            "den builder": (SkillPath.CAMP, 2),
            "signature": (SkillPath.OMEN, 3),
            "dream manager": (SkillPath.DREAM, 2),
            "it is not surprising": (SkillPath.CLAIRVOYANT, 2),
            "ATM": (SkillPath.PROPHET, 3),
            "guardian of culture": (SkillPath.LORE, 2),
            "natural instinct": (SkillPath.SENSE, 2),

        }
        
        old_skill = old_skill.strip()
        if old_skill in conversion:
            new_skill.primary = Skill(conversion[old_skill][0])
            new_skill.primary.set_points_to_tier(conversion[old_skill][1])
        else:
            new_skill = CatSkills.generate_new_catskills(status, moons)
        
        return new_skill


        
            

        